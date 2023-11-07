# Hello, slackbot!

## requirements
- Python 3.9
- `pip install requirements.txt`

## Adding new app to the Slack workspace
- visit [https://api.slack.com/apps](https://api.slack.com/apps)
- follow the process

- set configs appropriately:
  - `SLACK_BOT_USER_OAUTH_TOKEN` from `Bot User OAuth Token` from `Features: OAuth & Permissions > OAuth Tokens for Your Workspace`

  - ![oauth_token image](assets/oauth_token.png)

  - `SLACK_APP_ID` from `Settings: Basic Information > App Credentials > App ID`
  - `SLACK_CLIENT_ID` from `App Credentials > Client ID`
  - `SLACK_CLIENT_SECRET` from `App Credentials > Client Secret`
  - `SLACK_SIGNING_SECRET` from `App Credentials > Signing Secret`

  - ![app_credentials image](assets/app_credentials.png)

## How to run
- `python async_write.py`
  - ![async_write example image](assets/async_write.png)
  - simply writing a text to certain channel
  - requires `chat:write`

- `python upload.py`
  - ![upload example image](assets/upload.png)
  - uploads a file specified by `--filepath` to slack, defaults to `./tmp.txt`
  - requires `files:write` / also requires `files.read` permission to check uploaded content

- `python event.py`
  - `ngrok http 8000 --oauth google`
  - visit slack api's `Features > Event Subscriptions` tab and enter url provided by ngrok
  - solve ["challenge"](https://api.slack.com/events/url_verification) by temporarily uncommenting `@app.route("/slack/events")` code block
    - definitely we need a better way, but since it is one-time job...
  - `Subscribe to bot events`
    - `app_mention`
      - ![event:app_mention example image](assets/event__app_mention.png)
    - `message.channels`
      - ![event:message_channels example image](assets/event__message_channels.png)
    - `reaction_added`
      - ![event:reaction_added example image](assets/event__reaction_added.png)
  - Monitor incoming events from `http://localhost:4040`

## To Refer
- https://slack.dev/python-slack-sdk/api-docs/slack_sdk/
- https://api.slack.com/methods
- https://github.com/slackapi/python-slack-events-api
