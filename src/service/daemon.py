import twitchio
import asyncio
import json
import time
import threading as th
from websockets.server import serve
from websocket import create_connection
from youtube import YouTube
from pprint import pprint

BOT_USERNAME = 'AQUASINE'
CHANNEL_NAMES = ['AQUASINE', 'brggren', 'jarvisjohnson']
YOUTUBE_CHANNELS = {
    'UCujyjxsq5FZNVnQro51zKSQ': 'fuslie'}
YOUTUBE_FETCH_INTERVAL = 1

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
        return await super().event_ready()

    async def event_error(self, error: Exception, data: str = None):
        # print(error)
        return await super().event_error(error, data)

    async def event_message(self, message):
        await process_message('ttv', message.channel.name, message.author.name, message.content)


async def run_youtube():
    t = YouTube()
    t.youtube_connect(list(YOUTUBE_CHANNELS.keys())[0])
    while True:
        messages = t.twitch_receive_messages()
        for msg in messages:
            await process_message('yt', msg['channelId'], msg['username'], msg['message'])
        time.sleep(YOUTUBE_FETCH_INTERVAL)

connected_websockets = []

async def process_message(type, channel, user, message):
    # send message to all connected websockets
    channel_name = channel
    if type == 'yt':
        channel_name = YOUTUBE_CHANNELS[channel]
    print(f"type: {type}, channel: {channel_name}, user: {user}, message: {message}")
    obj_message = json.dumps({
        'type': type,
        'channel': channel,
        'channel_name': channel_name,
        'user': user,
        'message': message,
        'weight': 1.0,
        'tags': [type, type + ":" + channel]
    })
    await send_message(obj_message)


async def ws_handler(websocket, path):
    connected_websockets.append(websocket)
    try:
        async for message in websocket:
            pass
    finally:
        connected_websockets.remove(websocket)

async def send_message(message):
    for ws in connected_websockets:
        await ws.send(message)

def run_bot(bot):
    bot.run()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start_server = serve(ws_handler, "localhost", 8765)
    loop.run_until_complete(start_server)

    # start youtube thread
    yt_thread = th.Thread(target=asyncio.run, args=(run_youtube(),))
    yt_thread.start()
    
    bot = Bot()
    bot.run()


