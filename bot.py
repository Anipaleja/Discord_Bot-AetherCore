import discord
from discord.ext import commands
import json
import os

# Load config
with open('config.json') as f:
    config = json.load(f)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

# Load Cogs
for cog in ['moderation', 'stats', 'music', 'reminders']:
    bot.load_extension(f'cogs.{cog}')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(config["token"])
