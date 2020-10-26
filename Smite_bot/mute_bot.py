# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
has_god = False
prev_god = ""
@bot.command(name='mute', help='mute users')   
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    guild = ctx.guild
    if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.add_roles(role)
        await ctx.send(f"🔨{member} was muted.")
    else:
        await member.add_roles(role) 
        await ctx.send(f"🔨{member} was muted.")     

@bot.command(name='mute', help='mute users')   
async def unmmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    guild = ctx.guild
    if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.add_roles(role)
        await ctx.send(f"🔨{member} was unmuted.")
    else:
        await member.remove_role(role) 
        await ctx.send(f"🔨{member} was unmuted.")     