import random

class PodiumConfiguration():
    def __init__(self, id, twitch_channels=[], youtube_channels={}, rules=[]):
        self.id = id
        self.twitch_channels = twitch_channels
        self.youtube_channels = youtube_channels
        self.rules = rules

class PodiumRule():
    def __init__(self, condition=None, action=None):
        self.condition = condition
        self.action = action

    def process_message(self, result):
        if self.action is None:
            return result
        do_action = self.condition is None or self.condition(result)
        if do_action:
            return self.action(result)
        return result

class PodiumRuleResult():
    def __init__(self, message, score, tags, metadata):
        self.message = message
        self.score = score
        self.tags = tags
        self.metadata = metadata

def random_score(result):
    # Random score between 0 and 1
    result.score = random.random()

