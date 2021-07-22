from dotenv import load_dotenv
load_dotenv()

import os
bot_token = os.environ.get("bot-token")

from discord.ext import commands
import discord

from core import Core

# Create a bot instance with prefix of ,
bot = commands.Bot(command_prefix=',', help_command=None)

# On connection ready event
@bot.event
async def on_ready():
    # Log to console that we've logged in successfully
    print('Logged in as: {0.user}'.format(bot))

# On message event
@bot.event
async def on_message(message):
    # Checking if message event was triggered by self
    if message.author == bot.user:
        return

    # Process the bot commands after our message actions are done
    await bot.process_commands(message)

bot.add_cog(Core(bot))

bot.run(bot_token)
