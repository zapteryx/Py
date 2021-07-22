import asyncio
from datetime import datetime

from random import randint

from discord.ext import commands
from discord import Embed

class Reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.users = []
    
    @commands.command()
    async def reaction(self, ctx):
        if ctx.author.id in self.users:
            await ctx.send("can't start while in progress!")
            return
        self.users.append(ctx.author.id)
        embed = Embed(title="Reaction", description="test your reaction speed!\n\nget ready the word `Py`, and hit `[Send]` when I tell you to!")
        await ctx.send(embed=embed)
        time_to_wait = randint(3, 8)
        await asyncio.sleep(time_to_wait)
        probe = await ctx.send("%s, hit send now!" % ctx.author.mention)
        start = datetime.now()
        def message_check(m):
            return m.content.lower() == "py" and m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
        try:
            msg = await self.bot.wait_for('message', check=message_check, timeout=5.0)
            now = datetime.now()
        except asyncio.TimeoutError:
            await probe.edit(content="%s, too late!" % ctx.author.mention)
        else:
            await probe.edit(content="%s, time: `%.2fms`" % (ctx.author.mention, (now - start).total_seconds() * 1000))
        finally:
            self.users.remove(ctx.author.id)
