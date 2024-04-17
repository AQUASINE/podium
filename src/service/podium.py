import random
import asyncio
import re
import nltk
nltk.download([
    "stopwords",
    "vader_lexicon",
    'brown'
])
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from detoxify import Detoxify

class PodiumConfiguration():
    def __init__(self, id, twitch_channels=[], youtube_channels={}, rules=[]):
        self.id = id
        self.twitch_channels = twitch_channels
        self.youtube_channels = youtube_channels
        self.rules = rules

class PodiumRule():
    def __init__(self, condition=None, action=None, name=""):
        self.name = name
        self.condition_args = []
        self.action_args = []
        self.action = None
        self.condition = lambda x: True

        if condition is not None:
            self.condition = condition[0]
            if len(condition) > 1:
                self.condition_args = condition[1:]

        if action is not None:
            self.action = action[0]
            if len(action) > 1:
                self.action_args = action[1:]

    async def process_message(self, result):
        if self.action is None:
            return result
        
        if len(self.condition_args) == 0:
            do_action = await self.run_async(self.condition, result)
        else:
            do_action = await self.run_async(self.condition, result, *self.condition_args)

        if do_action:
            if len(self.action_args) == 0:
                return await self.run_async(self.action, result)
            return await self.run_async(self.action, result, *self.action_args)
        return result
    
    async def run_async(self, func, *args, **kwargs):
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        return func(*args, **kwargs)

class PodiumRuleResult():
    def __init__(self, message, score, user_id, tags, metadata):
        self.message = message
        self.score = score
        self.tags = tags
        self.user_id = user_id
        self.metadata = metadata
        self.ready_next = False
    
    def __str__(self) -> str:
        return f"Message: {self.message}, Score: {self.score}, Tags: {self.tags}, Metadata: {self.metadata}"

def random_score(result):
    # Random score between 0 and 1
    result.score = random.random()
    result.ready_next = True

def set_score(result, val):
    result.score = val
    result.ready_next = True

def multiply_score(result, val):
    result.score *= val
    result.ready_next = True

def divide_score(result, val):
    result.score /= val
    result.ready_next = True

def add_score(result, val):
    result.score += val
    result.ready_next = True

def subtract_score(result, val):
    result.score -= val
    result.ready_next = True

analyzer = SentimentIntensityAnalyzer()
def analyze_sentiment(result, complete_funcs):
    message = result.message
    # remove stop words
    words = [word for word in message.split() if word.lower() not in nltk.corpus.stopwords.words('english')]
    message = ' '.join(words)
    
    sentiment_scores = analyzer.polarity_scores(message)
    score = sentiment_scores['compound']

    for complete_func in complete_funcs:
        complete_func(result, score)

users = {}
def add_user_score(result, score):
    users[result.user_id]['user_score'] += score

def cond_probability(result, chance):
    return random.random() <= chance

def cond_has_tag(result, tag):
    return tag in result.tags

def cond_exact_match(result, match):
    result = result.message.strip()
    match = match.strip()
    return result == match

def cond_contains(result, match):
    result = result.message.strip()
    match = match.strip()
    return match in result

def cond_contains_any(result, matches):
    result = result.message.strip()
    for match in matches:
        match = match.strip()
        if match in result:
            return True
    return False

detox = Detoxify('original')
def cond_toxicity(result, threshold):
    tox_result = detox.predict(result.message)
    toxicity = tox_result['toxicity']
    severe_toxicity = tox_result['severe_toxicity']
    return toxicity >= threshold or severe_toxicity >= threshold

def cond_regex(result, regex):
    return re.search(regex, result.message) is not None

def compare_value(value1, value2, operator):
    if operator == '==':
        return value1 == value2
    elif operator == '!=':
        return value1 != value2
    elif operator == '>':
        return value1 > value2
    elif operator == '<':
        return value1 < value2
    elif operator == '>=':
        return value1 >= value2
    elif operator == '<=':
        return value1 <= value2
    return False

def cond_message_length(result, operator, length):
    return compare_value(len(result.message), length, operator)

def cond_score(result, operator, score):
    return compare_value(result.score, score, operator)

def cond_logic_not(result, func):
    return not func(result)

def cond_logic_and(result, func1, func2):
    return func1(result) and func2(result)

def cond_logic_or(result, func1, func2):
    return func1(result) or func2(result)

def cond_logic_xor(result, func1, func2):
    return func1(result) ^ func2(result)

def action_set_tag(result, tag):
    result.tags.append(tag)

def action_remove_tag(result, tag):
    result.tags.remove(tag)
    
def action_set_metadata(result, key, value):
    result.metadata[key] = value

def action_remove_metadata(result, key):
    del result.metadata[key]

def action_remove_emotes(result, emotes):
    # remove any instances of emotes from the message
    for emote in emotes:
        result.message = result.message.replace(emote, '')


async def gpt_score(result, gpt_client, complete_func, default=0.0):
    result.ready_next = False
    gpt_client.enqueue_for_eval(result)
    while gpt_client.is_in_queue(result):
        await asyncio.sleep(0.1)
    score = default
    if result.metadata.get('gpt_score') is not None:
        score = result.metadata['gpt_score']

    # use this to update score, or do any other operation
    complete_func(result, score)

    result.ready_next = True
