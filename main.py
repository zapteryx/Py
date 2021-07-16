from dotenv import load_dotenv
load_dotenv()

import os
bot_token = os.environ.get("bot-token")

from discord.ext.commands import Bot

# client = discord.Client()
client = Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

client.run(bot_token)
