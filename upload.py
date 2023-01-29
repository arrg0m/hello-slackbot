import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from config import config

client = WebClient(token=config['SLACK_BOT_USER_OAUTH_TOKEN'])

try:
    filepath="./tmp.txt"
    response = client.files_upload_v2(
        filename='custom_filename',
        file=filepath,
        title='custom_title',
        channel=config['RANDOM_CHANNEL_ID'],
        request_file_info=True  # requires `files:read` permission to access uploaded file
    )
    assert response["file"]  # the uploaded file
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
