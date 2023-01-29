import asyncio
import os
from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.errors import SlackApiError


from config import config

client = AsyncWebClient(token=config['SLACK_BOT_USER_OAUTH_TOKEN'])

async def post_message():
    text_message = 'Hello World!'
    try:
        response = await client.chat_postMessage(
            channel=config['GENERAL_CHANNEL_ID'],
            text=text_message
        )
        assert response["message"]["text"] == text_message
    except SlackApiError as e:
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")

asyncio.run(post_message())

