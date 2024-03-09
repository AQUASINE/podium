import random
import asyncio

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
    def __init__(self, message, score, tags, metadata):
        self.message = message
        self.score = score
        self.tags = tags
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

def cond_probability(result, chance):
    return random.random() <= chance

def cond_tag(result, tag):
    return tag in result.tags

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

