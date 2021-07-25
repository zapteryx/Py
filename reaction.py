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
    async def reaction(self, ctx, *args):
        if len(args) > 1:
            await ctx.send("too many arguments! supported argument(s): `multiple`")
            return
        if ctx.author.id in self.users:
            await ctx.send("can't start while in progress!")
            return
        self.users.append(ctx.author.id)
        multiple = False
        reactions = ["1️⃣"]
        if len(args) > 0 and args[0].lower() == "multiple":
            multiple = True
            reactions.append("2️⃣")
            reactions.append("3️⃣")
        embed = Embed(title="Reaction", description="test your reaction speed!\nreact to my message with the reaction when I tell you to!")
        initial = await ctx.send(embed=embed)
        for reaction in reactions:
            await initial.add_reaction(reaction)
        random_reaction = randint(0, len(reactions) - 1)
        time_to_wait = randint(3, 8)
        await asyncio.sleep(time_to_wait)
        probe = await ctx.send("%s, react with %s now!" % ctx.author.mention, reactions[random_reaction])
        start = datetime.now()
        def reaction_check(reaction, user):
            return user.id == ctx.author.id and str(reaction.emoji) == reactions[random_reaction]
        try:
            await self.bot.wait_for('reaction_add', check=reaction_check, timeout=5.0)
            now = datetime.now()
        except asyncio.TimeoutError:
            await probe.edit(content="%s, too late!" % ctx.author.mention)
        else:
            await probe.edit(content="%s, time: `%.2fms`" % (ctx.author.mention, (now - start).total_seconds() * 1000))
        finally:
            self.users.remove(ctx.author.id)
