import twitchio
import asyncio
import json
import time
import threading as th
from podium import *
from flask import Flask
from gptclient import GPTClient
from websockets.server import serve
from websocket import create_connection
from youtube import YouTube
from pprint import pprint

BOT_USERNAME = 'AQUASINE'
YOUTUBE_FETCH_INTERVAL = 1

# read bot token from config.json. if it doesn't exist, tell the user to create it
with open('config.json', 'r') as f:
    config = json.load(f)
    try:
        BOT_TOKEN = config['TWITCH_OAUTH']
    except KeyError:
        print("config.json is missing the TWITCH_OAUTH key. Please create a bot account and add the OAuth token to config.json")
        exit(1)
    try:
        OPENAI_KEY = config['OPENAI_KEY']
    except KeyError:
        print("config.json is missing the OPENAI_KEY key. Please create an OpenAI API key and add it to config.json")
        exit(1)

gpt_client = GPTClient(OPENAI_KEY)

DEFAULT_RULES = [
    PodiumRule(
        name="Set Score",
        action=[set_score, 10]
        ),
    PodiumRule(
        name="GPT multiply",
        action=[gpt_score, gpt_client, multiply_score, 0.5]
    )
]
DEFAULT_CONFIGURATION = PodiumConfiguration('Default', ['jerma985'], {'UCujyjxsq5FZNVnQro51zKSQ': 'fuslie','UCMnULQ5F6kLDAHxofDWIbrw': 'PirateSoftware'}, DEFAULT_RULES)

configurations = [DEFAULT_CONFIGURATION]
active_configuration = DEFAULT_CONFIGURATION

class Bot(twitchio.Client):
    def __init__(self):
        super().__init__(token=BOT_TOKEN, initial_channels=[])

    async def event_channel_joined(self, channel: twitchio.Channel):
        print(f'TTV: Joined {channel.name}')
        return await super().event_channel_joined(channel)

    async def event_ready(self):
        print('Daemon is ready to connect to Twitch channels.')
        await self.join_channels(active_configuration.twitch_channels)
        return await super().event_ready()

    async def event_error(self, error: Exception, data: str = None):
        print(error)
        return await super().event_error(error, data)

    async def event_message(self, message):
        await process_message('ttv', message.channel.name, message.author.name, message.content)


async def run_youtube():
    t = YouTube()
    channel_id = list(active_configuration.youtube_channels.keys())[0]
    channel_name = active_configuration.youtube_channels[channel_id]
    t.youtube_connect(channel_id, channel_name)
    while True:
        messages = t.twitch_receive_messages()
        for msg in messages:
            await process_message('yt', msg['channelId'], msg['username'], msg['message'])
        time.sleep(YOUTUBE_FETCH_INTERVAL)

connected_websockets = []

processing_messages = []

users = []
recent_messages = []

def add_recent_message(message):
    recent_messages.append(message)
    if len(recent_messages) > 500:
        recent_messages.pop(0)
        
def set_user_recent(type, user, message):
    # object with type, user, message, timestamp, and user_score
    user_obj = None
    for u in users:
        if u['user'] == user:
            user_obj = u
            break
    if user_obj is None:
        user_obj = {'type': type, 'user': user, 'last_message': message, 'timestamp': time.time(), 'user_score': 0}
        users.append(user_obj)
    else:
        user_obj['last_message'] = message
        user_obj['timestamp'] = time.time()

async def process_message(type, channel, user, message):
    # send message to all connected websockets
    channel_name = channel
    id_tag = None
    if type == 'yt':
        channel_name = active_configuration.youtube_channels[channel]
        id_tag = f"ytid:{channel}"
    tags = [type, type + ":" + channel_name]
    if id_tag is not None:
        tags.append(id_tag)

    add_recent_message(message)
    set_user_recent(type, user, message)

    result = PodiumRuleResult(message, 1.0, tags, {})
    now = time.time()

    # print('new message', type, channel, user, message)
    obj_message = json.dumps({
        'type': type,
        'channel': channel,
        'channel_name': channel_name,
        'user': user,
        'message': message,
        'weight': 0,
        'timestamp': time.time(),
        'tags': tags
    })

    processing_entry = {
        'timestamp': now,
        'result': result,
        'rule': 0,
        'started': False,
        'obj': obj_message
    }
    processing_messages.append(processing_entry)
    

async def process_periodic():
    print("Processing periodic")
    while True:
        await asyncio.sleep(0.05)
        await execute_processing()

async def execute_processing():
    if len(active_configuration.rules) == 0:
        return
    
    for entry in processing_messages:
        # if the message is too old, throw it out
        if time.time() - entry['timestamp'] > 60:
            processing_messages.remove(entry)
            continue

        result = entry['result']
        
        if entry['rule'] == 0 and not entry['started']:
            rule = active_configuration.rules[entry['rule']]    
            asyncio.create_task(rule.process_message(result))
            entry['started'] = True
            
            
        elif result.ready_next:
            entry['rule'] += 1
            if entry['rule'] >= len(active_configuration.rules):
                await finish_processing_entry(entry)
                continue
        
            rule = active_configuration.rules[entry['rule']]
            asyncio.create_task(rule.process_message(result))
        

async def finish_processing_entry(entry):
    obj = entry['obj']
    score = float(entry['result'].score)
    metadata = entry['result'].metadata

    # replace the score with the new score
    obj = json.loads(obj)
    obj['weight'] = score
    obj['metadata'] = metadata
    print(obj)

    processing_messages.remove(entry)
    
    await send_message(json.dumps(obj))


async def ws_handler(websocket, path):
    print("new websocket connection")
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

app = Flask(__name__)

@app.route('/')
def get_twitch_channels():
    return json.dumps(active_configuration.twitch_channels)

@app.route('/reconnect')
def reconnect():    
    global yt_thread, ttv_thread, bot
    # stop threads
    print("join youtube thread")
    yt_thread.join()
    print("join twitch thread")
    bot.close()
    ttv_thread.join()

    print("close bot")
    # stop bot

    print("reconnect")
    connect()

processing_thread = None
gpt_thread = None
yt_thread = None
ttv_thread = None
bot = None

async def run_gpt():
    await gpt_client.process_queue()
    
def connect():
    # start youtube thread
    global yt_thread, ttv_thread, gpt_thread, bot
    yt_thread = th.Thread(target=asyncio.run, args=(run_youtube(),))
    yt_thread.start()

    bot = Bot()
    ttv_thread = th.Thread(target=run_bot, args=(bot,))
    ttv_thread.start()

    gpt_thread = th.Thread(target=asyncio.run, args=(run_gpt(),))
    gpt_thread.start()

    processing_thread = th.Thread(target=asyncio.run, args=(process_periodic(),))
    processing_thread.start()
    


# if __name__ == "__main__":
loop = asyncio.get_event_loop()
start_server = serve(ws_handler, "localhost", 8765)
loop.run_until_complete(start_server)

connect()
run_gpt()

while True:
    pass