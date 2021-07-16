from dotenv import load_dotenv
load_dotenv()

import os
bot_token = os.environ.get("bot-token")

import discord
from discord.ext.commands import Bot

# client = discord.Client()
client = Bot(".")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)} ms')

bot.run(bot_token)