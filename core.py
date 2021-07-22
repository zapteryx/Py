from discord.ext import commands
from discord import Embed

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def about(ctx):
        embed = Embed(title="Py", description="a bot made with ❤️ and python\n\ndeveloped by **zapteryx**, **QuackNoodels121**, **Inquisitives**\nopen source at https://github.com/zapteryx/Py")
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong! (%i ms)' % round(self.bot.latency * 1000))
