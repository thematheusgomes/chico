import os
import json
from urllib.parse import parse_qsl
from slack import WebClient
from slack.errors import SlackApiError
from src.collect_data import select
from src.log import Logger
from src.cards import test_message

LOG = Logger()

SLACK_TOKEN = os.getenv('SLACK_TOKEN')

def main(event, context):
    client = WebClient(token=SLACK_TOKEN)
    params = dict(parse_qsl(event["body"]))
    LOG.info(params)
    # result = select(params['text'])
    # for row in result:
        # msg = message(row)
    card = test_message()
    try:    
        client.chat_postMessage(channel='#dev-fraud-watch', blocks=card)
        return {
            "statusCode": 200,
            "body": json.dumps({
                "text": "done"
            })
        }
    except SlackApiError as e:
        LOG.error(f'Error: {e}')
        return {
            "statusCode": 500,
            "body": json.dumps({
                "text": "failed"
            })
        }

# def message(result):
#     return f"""
# TID: {result[0]}
# User: {result[1]}
# Transaction: {result[2]}
# Status: {result[3]}
# Event: {result[4]}
# """
