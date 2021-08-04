from datetime import datetime

from discord.ext import commands
from discord import Embed

class Core(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db
    
    @commands.command()
    async def about(self, ctx):
        embed = Embed(title="Py", description="a bot made with ❤️ and python\n\ndeveloped by **zapteryx**, **QuackNoodels121**, **Inquisitives**\nopen source at https://github.com/zapteryx/Py")
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        if self.db != None:
            start = datetime.now()
            async with self.db.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("SELECT 1")
                    await cursor.fetchall()
                    now = datetime.now()
                    await ctx.send('Pong! (API: %i ms, DB: %i ms)' % (round(self.bot.latency * 1000), (now - start).total_seconds() * 1000))
        else:
            await ctx.send('Pong! (API: %i ms)' % round(self.bot.latency * 1000))