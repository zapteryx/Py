from dotenv import load_dotenv
load_dotenv()

import os
bot_token = os.environ.get("bot-token")

from discord.ext.commands import Bot

from core import Core
from reaction import Reaction

# Create a bot instance with prefix of ,
bot = Bot(command_prefix=',', help_command=None)

# On connection ready event
@bot.event
async def on_ready():
    # Log to console that we've logged in successfully
    print('Logged in as: %s' % bot.user)

# On message event
@bot.event
async def on_message(message):
    # Checking if message event was triggered by self
    if message.author == bot.user:
        return

    # Process the bot commands after our message actions are done
    await bot.process_commands(message)

bot.add_cog(Core(bot))
bot.add_cog(Reaction(bot))

bot.run(bot_token)
