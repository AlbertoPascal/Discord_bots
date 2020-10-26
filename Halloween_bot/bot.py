# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
import discord
from discord.ext.commands import has_permissions, CheckFailure
import asyncio
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL


load_dotenv()
token = os.getenv("DISCORD_TOKEN")
Client = discord.Client()
bot = commands.Bot(command_prefix = ".")

@bot.command(name = "play2",pass_context = True)
async def play2(ctx, url):
    channel = ctx.message.author.voice.channel
    print("my channel was ", channel)
    await ctx.send(channel)
    voice = await channel.connect()
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    #voice = get(Client.voice_clients, guild=ctx.guild)
    
    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            args = ctx.message.content.split(" ")
            betterargs = " ".join(args[1:])
            #info = ydl.extract_info('https://www.youtube.com/watch?v=' + betterargs, download=False)
            info = ydl.extract_info('https://www.youtube.com/watch?v=zczFoOBe1eQ', download = False)
        URL = info['formats'][0]['url']
        voice.source = discord.PCMVolumeTransformer(voice.source, volume=1.0)
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
    else:
        await ctx.send("Already playing song")
        return
    
    
@bot.command(name = "play" , pass_context=True)
async def play(ctx):
    channel = ctx.message.author.voice.channel
    print("my channel was ", channel)
    await ctx.send(channel)
    voice = await channel.connect()
    await channel.self_deaf(True)
    args = ctx.message.content.split(" ")
    betterargs = " ".join(args[1:])
    #player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=' + betterargs)
   
    player.start()
  
@bot.command(name='age', help = 'Gets the user creation date')
async def get_age(ctx, member: discord.Member):
    await ctx.send(str(member) + "'s account was created at: " + str(member.created_at))
    
@bot.command(name='test', help = 'test sending commands')
async def get_age(ctx):
    await ctx.send('-p zeus destripando historia')
    
   
bot.run(token)