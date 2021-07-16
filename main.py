from dotenv import load_dotenv
load_dotenv()

import os
bot_token = os.environ.get("bot-token")

from discord.ext import commands

# client = discord.Client()
bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@commands.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)} ms')

bot.add_command(ping)

bot.run(bot_token)
