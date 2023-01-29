# Hello, slackbot!

## requirements
- Python 3.9
- `pip install requirements.txt`

## Adding new app to the Slack workspace
- visit https://api.slack.com/app
- follow the process

- set configs appropriately:
  - `SLACK_BOT_USER_OAUTH_TOKEN` from `Bot User OAuth Token` from `Features > OAuth & Permissions > OAuth Tokens for Your Workspace`

  - `SLACK_APP_ID` from `Settings > Basic Information > App Credentials > App ID`
  - `SLACK_CLIENT_ID` from `App Credentials > Client ID`
  - `SLACK_CLIENT_SECRET` from `App Credentials > Client Secret`
  - `SLACK_SIGNING_SECRET` from `App Credentials > Signing Secret`

## How to run
- `python async_write.py`
  - requires `chat:write`
- `python upload.py`
  - require `files:write`
  - require `files.read` to check uploaded content
