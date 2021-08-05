from dotenv import load_dotenv
load_dotenv()

import os
bot_token = os.environ.get("bot-token")
assert bot_token != None, "Bot token not specified."
prefix = ',' if os.environ.get("prefix") == None else os.environ.get("prefix")
sql_info = {"host": os.environ.get("db-host"), "port": 3306 if os.environ.get("db-port") == None else os.environ.get("db-port"), "username": os.environ.get("db-username"), "password": os.environ.get("db-password"), "database": os.environ.get("db-database")}

for key in sql_info:
    if sql_info[key] == None:
        sql_info = None
        break

import aiomysql, asyncio

async def initialize_db(sql_info):
    if sql_info == None:
        db = None
    else:
        db = await aiomysql.create_pool(
            host=sql_info["host"],
            port=sql_info["port"],
            user=sql_info["username"],
            password=sql_info["password"],
            db=sql_info["database"],
            autocommit=True
        )
    return db

loop = asyncio.get_event_loop()
try:
    db = loop.run_until_complete(initialize_db(sql_info))
    if db == None:
        print("Database information not provided (or partially missing), disabling support.")
    else:
        print("Database support enabled!")
except aiomysql.OperationalError as err:
    print("Disabling database support as an error occurred during attempt to connect:\n%s" % err)
    db = None

from discord.ext.commands import Bot

from core import Core
from reaction import Reaction

# Create a bot instance with prefix of , if not specified
bot = Bot(command_prefix=prefix, help_command=None)

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

bot.add_cog(Core(bot, db))
bot.add_cog(Reaction(bot))

print('Attempting connection to Discord...')
bot.run(bot_token)
