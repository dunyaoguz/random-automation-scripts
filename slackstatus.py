# script to update slack status with a random cat fact
import os
import sys
import requests
import random
import json
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

SLACK_TOKEN = os.environ['SLACK_TOKEN']

def get_cat_fact():
    url = 'https://catfact.ninja/fact'
    response = requests.get(url)
    fact = response.json()['fact']
    return fact

def update_status(fact):
    json = {
        "profile": {
            "status_text": fact
        }
    }
    header = {
        'Authorization': 'Bearer ' + SLACK_TOKEN,
        'Content-Type': 'application/json'
    }
    URL = "https://slack.com/api/users.profile.set"
    response = requests.post(URL, json=json, headers=header)
    return response

if __name__ == '__main__':
    fact = get_cat_fact()
    update_status(fact)
