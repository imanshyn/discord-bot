import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import ctypes.util
import os
from asyncio import Queue

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
queue = Queue()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    opus_path = ctypes.util.find_library('opus')
    if opus_path:
        discord.opus.load_opus(opus_path)
    else:
        print("Opus library path not set. Please set the OPUS_LIB_PATH environment variable.")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not connected to a voice channel.")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()

@bot.command()
async def skip(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("Skipped the current track.")
    else:
        await ctx.send("No track is currently playing.")

@bot.command()
async def play(ctx, url):
    await queue.put(url)
    await ctx.send(f"Added to queue: {url}")
    if not ctx.voice_client.is_playing():
        await play_next(ctx)

async def play_next(ctx):
    if not queue.empty():
        url = await queue.get()
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2)
            ctx.voice_client.play(source, after=lambda e: bot.loop.create_task(play_next(ctx)))
    else:
        await ctx.send("Queue is empty.")

bot.run(os.getenv('BOT_TOKEN'))