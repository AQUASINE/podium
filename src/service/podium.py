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

    def process_message(self, message):
        if self.action is None:
            return
        do_action = self.condition is None or self.condition(message)
        if do_action:
            self.action(message)

