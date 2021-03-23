import json
from urllib.parse import parse_qsl
from src.log import Logger
from src.bot_commands.commands import commands_handler
from src.slack_messages.messages import message_handler

log = Logger()

def main(event, context):
    payload = dict(parse_qsl(event["body"]))
    log.info(f"Event: {json.dumps(payload)}")
    commands_handler(payload['command'], payload['text'])
    return message_handler(log)
