
from openai import OpenAI
from podium import *
from json_repair import repair_json
import time
import json
import random
import asyncio

class GPTClient():
    def __init__(self, api_key) -> None:
        self.client = OpenAI(api_key=api_key)
        self.prompt = "These are messages sent in Jerma985's Twitch chat. Find the funny messages. This could be a joke, or just something that makes you laugh."
        self.ttl = 16
        self.time_between_evals = 8
        self.num_oldest_to_process = 10
        self.num_other_to_process = 10
        self.last_eval = time.time()
        self.queue = []
        self.in_process = []
        self.is_running = False
    
    def set_prompt(self, prompt):
        self.prompt = prompt

    def process_messages(self, prompt, results):
        self.is_running = True
        context = '''
I have the following messages that I would like to give a value from 0 to 1 based on how well it fits this prompt: 
"'''
        context += prompt
        context += '''"
        
Each of these messages are labeled with an id followed by a message, like this:
a559df:  message content

Please give the value in json format, where it is an array of objects that match the format:
{ "id": "a559df", "score": 0.554 }
Do not include any other text in the response besides the object. Please be specific with the weighting and go down to the third decimal place. Remember, the prompt is: 
"'''
        context += prompt
        context += '''"
Now, here are the messages:
'''

        messages_string = ""
        # generate an 8 character id for each message using lowercase, uppercase, and digits
        id_to_result = {}
        for result in results:
            id = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
            messages_string += id + ": " + result.message + "\n"
            id_to_result[id] = result

        context += messages_string
        
        # print(context)
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": context
                }
            ]
        )
        text = response.choices[0].message.content
        print(text)
        text = repair_json(text)
        self.is_running = False
        try:
            entries = json.loads(text)
            for entry in entries:
                result = id_to_result[entry['id']]
                result.metadata['gpt_score'] = entry['score']
                print("GPT Score for message: " + result.message + " is " + str(entry['score']))
                print(result)
        except Exception as e:
            print("Error parsing GPT response")
            print(e)
            print(text)
            pass
        finally:
            self.in_process = []


    def enqueue_for_eval(self, result):
        # get timestamp, which will be used to find entries past ttl
        now = time.time()
        self.queue.append((now, result))
    
    def is_in_queue(self, result):
        for entry in self.queue:
            if entry[1] == result:
                return True
        for entry in self.in_process:
            if entry == result:
                return True
        return False
        
        
    async def process_queue(self):
        print("Processing GPT queue")
        while True:
            if self.is_running:
                await asyncio.sleep(0.2)
                continue
            
            time_between_full_checks = 0.2
            full_check_times = self.time_between_evals / time_between_full_checks
            for i in range(int(full_check_times)):
                if len(self.queue) >= self.num_oldest_to_process + self.num_other_to_process:
                    break
                await asyncio.sleep(time_between_full_checks)
            
            print("Queue currently has " + str(len(self.queue)) + " entries")

            # go through the queue and process any entries that are past the ttl
            now = time.time()
            to_remove = []
            for entry in self.queue:
                if now - entry[0] > self.ttl:
                    to_remove.append(entry)
                    
            for entry in to_remove:
                self.queue.remove(entry)

            # pick n oldest entries to process
            to_process = []
            to_remove = []
            
            for entry in self.queue:
                if len(to_process) < self.num_oldest_to_process:
                    to_process.append(entry[1])
                    to_remove.append(entry)
                else:
                    break

            for entry in to_remove:
                self.in_process.append(entry[1])
                self.queue.remove(entry)
            
            # pick m random entries to process
            for i in range(self.num_other_to_process):
                if len(self.queue) == 0:
                    break
                entry = random.choice(self.queue)
                to_process.append(entry[1])
                self.in_process.append(entry[1])
                self.queue.remove(entry)

            
            if len(to_process) > 0:
                print("Processing the following messages")

                for result in to_process:
                    print(result.message)
                
                self.process_messages(self.prompt, to_process)
                print("Finished processing messages")
            
            
        
        

if __name__ == '__main__':
    with open('config.json', 'r') as f:
        try:
            config = json.load(f)
            API_KEY = config['OPENAI_KEY']
        except KeyError:
            print("config.json is missing the OPENAI_KEY key. Please create an OpenAI API key and add it to config.json")
            exit(1)

    gpt_client = GPTClient(API_KEY)
    gpt_client.set_prompt("a gamer would say this")
    gpt_client.enqueue_eval_async([
        PodiumRuleResult("I am an epic gamer", 0, [], {}),
        PodiumRuleResult("Video games are for nerds", 0, [], {}),
        PodiumRuleResult("KILL YOURSELF", 0, [], {}),
    ])

    
