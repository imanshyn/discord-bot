# Discord Bot

This is a Discord bot written in Python using the `discord.py` library. The bot can join and leave voice channels, and play audio from YouTube links.

## Features

- Join voice channels
- Leave voice channels
- Play audio from YouTube links
- Add links to a queue
- Skip the current link

## Requirements

- Python 3.9+
- `discord.py`
- `yt-dlp`
- `pynacl`
- `ffmpeg`
- `libopus`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/discord-bot.git
    cd discord-bot
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Install `ffmpeg` and `libopus`:
    ```bash
    # On macOS using Homebrew
    brew install ffmpeg opus

    # On Ubuntu/Debian
    sudo apt-get update
    sudo apt-get install -y ffmpeg libopus0
    ```

4. Set the `OPUS_LIB_PATH` environment variable:
    ```bash
    export OPUS_LIB_PATH=/usr/lib/x86_64-linux-gnu/libopus.so.0
    ```

5. Replace `BOT_TOKEN` in [bot.py](http://_vscodecontentref_/0) with your actual bot token.

## Adding the Bot to a Server

To add your bot to a server, follow these steps:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and select your application.
2. Navigate to the "OAuth2" tab.
3. Under "OAuth2 URL Generator", select the `bot` scope.
4. Under "OAuth2 URL Generator", select the necessary permissions for your bot.
5. Copy the generated URL and paste it into your browser.
6. Select the server you want to add the bot to and authorize it.

For more detailed instructions, refer to the [Discord.js Guide](https://discordjs.guide/preparations/adding-your-bot-to-servers.html#bot-invite-links).

## Getting the Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and select your application.
2. Navigate to the "Bot" tab.
3. Click "Copy" under the "TOKEN" section to get your bot token.

## Running the Bot

To run the bot, use the following command:
```bash
python bot.py
```
To run the bot as Docker container, use the following command:
```bash
docker build -t discord-bot .
docker run -e BOT_TOKEN=YOUR_BOT_TOKEN discord-bot
```

## Management Commands

- `/join` - Bot joins the voice channel.
- `/leave` - Bot leaves the voice channel.
- `/play <YouTube URL>` - Bot plays audio from the provided YouTube link.
- `/skip` - Skips the current playing audio.
