# remember to install discord.py by doing 'pip install discord.py' in your command terminal

import discord
from discord.ext import commands

# Create a prefix for the bot
bot = commands.Bot(command_prefix='!')

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Command example: !hello
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello!')

# Run the bot with the token
bot.run('YOUR_TOKEN_HERE')

