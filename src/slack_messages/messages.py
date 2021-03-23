import os
import json
from slack import WebClient
from slack.errors import SlackApiError
from src.slack_messages.cards import block

SLACK_TOKEN = os.getenv('SLACK_TOKEN')

def message_handler(log):
    client = WebClient(token=SLACK_TOKEN)
    message = block()
    try:    
        client.chat_postMessage(channel='#dev-fraud-watch', blocks=message)
        return {
            "statusCode": 200,
            "body": json.dumps({
                "text": "done"
            })
        }
    except SlackApiError as e:
        log.error(f'Error: {e}')
        return {
            "statusCode": 500,
            "body": json.dumps({
                "text": "failed"
            })
        }
