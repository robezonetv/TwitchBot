# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands

class responder(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hellooooooo(self, ctx: commands.Context):
        await ctx.send(f"Hello, {ctx.author.name}!")

    @commands.command()
    async def hi(self, ctx: commands.Context):
        await ctx.send(f"Hi, {ctx.author.name}!")

def prepare(bot: Bot):
    bot.add_cog(responder(bot))
