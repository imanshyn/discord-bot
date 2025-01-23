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

## Running the Bot

To run the bot, use the following command:
```bash
python bot.py
```
To run the bot as Docker container, use the following command:

```bash
docker build -t discord-bot .
docker run -e BOT_TOKEN=YOUR_BOT_TOKEN discord-bot