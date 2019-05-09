# script to update slack status with an emoji

import slack
import fire
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

SLACK_TOKEN = os.environ['SLACK_TOKEN']
client = slack.WebClient(token=SLACK_TOKEN)

def update_emoji(emoji):
    client.api_call('users.profile.set', json={
        "profile": {
            "status_emoji": emoji
        }})

if __name__ == '__main__':
    fire.Fire({'update': update_emoji})
