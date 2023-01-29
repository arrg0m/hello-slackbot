from pprint import pprint

from flask import Flask
from flask import request
from slackeventsapi import SlackEventAdapter
from slack_sdk.web import WebClient

from config import config

app = Flask(__name__)

slack_client = WebClient(config['SLACK_BOT_USER_OAUTH_TOKEN'])

"""
@app.route(config["SLACK_EVENTS_ENDPOINT"], methods=['POST'])
def challange() -> str:
    if (challenge := request.json.get('challenge')) is not None:
        return challenge
"""

@app.route("/", methods=['GET'])
def hello() -> str:
    return "Hello, world!"

slack_events_adapter = SlackEventAdapter(
    config["SLACK_SIGNING_SECRET"],
    config["SLACK_EVENTS_ENDPOINT"],
    app
)

@slack_events_adapter.on("app_mention")
def app_mention(event_data):
    pprint(event_data)
    message = event_data["event"]
    slack_client.chat_postMessage(
        channel=message["channel"],
        text=f"How can I help you, <@{message['user']}>?",
    )

@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    emoji = event_data["event"]["reaction"]
    print(emoji)

@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    if message.get("subtype") is None and "hi" in message.get('text'):
        channel = message["channel"]
        message = "Hello <@%s>! :tada:" % message["user"]
        slack_client.chat_postMessage(channel=channel, text=message)

if __name__ == "__main__":
    app.run(port=int(config["SLACK_APP_PORT"]))
