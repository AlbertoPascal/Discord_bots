# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
import discord
from discord.ext.commands import has_permissions, CheckFailure

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
has_god = False
prev_god = ""
  

@bot.command(name='age', help = 'Gets the user creation date')
async def get_age(ctx, member: discord.Member):
    #member = ctx.author
    await ctx.send(str(member) + "'s account was created at: " + str(member.created_at))
    
    

@bot.command(name = 'start', help = 'Mute all users in the current voice channel')
async def game_start(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Dead")
    guild = ctx.guild
    if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Dead", permissions=perms)
    
    channel = ctx.message.author.voice.channel
    guild = ctx.guild
    channel2 = discord.utils.get(guild.voice_channels, name="Muertinis")
    #print("Channel was ", channel2)
    for member in channel.members:
        if role in member.roles:
            await member.move_to(channel2)
            await member.edit(mute=False)
        else:    
            await member.edit(mute=True)
            await ctx.send(f"🔨{member} was muted.")

@bot.command(name = 'discussion', help = 'Unmute all users in the current voice channel')
async def pause_game(ctx):
    guild = ctx.guild
    channel = discord.utils.get(guild.voice_channels, name="Room1")
    channel2 = discord.utils.get(guild.voice_channels, name="Muertinis")
    #channel = ctx.message.author.voice.channel
    for member in channel.members:
        await member.edit(mute=False)
        await ctx.send(f"🔨{member} was unmuted.")
    for member in channel2.members:
        await member.edit(mute=True)
        await member.move_to(channel)
    
        
@bot.command(name = 'kill', help = 'Register a user as dead', pass_context=True)
async def kill(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Dead")
    guild = ctx.guild
   
    if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Dead", permissions=perms)
    await member.add_roles(role)
    await ctx.send(f"Registered {member}'s Death!")
    
@bot.command(name = 'restart', help = 'restart the game', pass_context=True)
async def revive(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Dead")
    guild = ctx.guild
    channel = discord.utils.get(guild.voice_channels, name="Room1")
    channel2 = discord.utils.get(guild.voice_channels, name="Muertinis")
    if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Dead", permissions=perms)
    for member in ctx.guild.members:
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.send(f"Brought {member}'s back from the dead!")
    for member in channel.members:
        await member.edit(mute=False)
    for member in channel2.members:
        await member.move_to(channel)
        await member.edit(mute=False)
bot.run(token)