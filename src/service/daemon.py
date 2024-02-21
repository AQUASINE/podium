import twitchio
import asyncio
import json
from pprint import pprint

BOT_USERNAME = 'AQUASINE'
CHANNEL_NAMES = ['AQUASINE', 'brggren']

# read bot token from config.json. if it doesn't exist, tell the user to create it
with open('config.json', 'r') as f:
    try:
        config = json.load(f)
        BOT_TOKEN = config['TWITCH_OAUTH']
    except KeyError:
        print("config.json is missing the TWITCH_OAUTH key. Please create a bot account and add the OAuth token to config.json")
        exit(1)

class Bot(twitchio.Client):
    def __init__(self):
        super().__init__(token=BOT_TOKEN, initial_channels=[])

    async def event_channel_joined(self, channel: twitchio.Channel):
        print(f'Joined {channel.name}')
        return await super().event_channel_joined(channel)

    async def event_ready(self):
        print('Daemon is ready to connect to Twitch channels.')
        await self.join_channels(CHANNEL_NAMES)
        print(f'Joined channels: {CHANNEL_NAMES}')
        return await super().event_ready()

    async def event_error(self, error: Exception, data: str = None):
        # print(error)
        return await super().event_error(error, data)

    async def event_message(self, message):
        print(f'channel: {message.channel.name}, user: {message.author.name}, message: {message.content}')
        

def run_bot(bot):
    bot.run()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    bot = Bot()
    bot.run()


