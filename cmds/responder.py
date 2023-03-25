# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands


class Responder(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hellooooooo(self, ctx: commands.Context):

        await ctx.send(f"Hello, {ctx.author.name}!")

    @commands.command()
    async def hi(self, ctx: commands.Context):
        await ctx.send(f"Hi, {ctx.author.name}!")


class Responder2(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def partoska(self, ctx: commands.Context):
        await ctx.send(f"EEEEEEEJ PARTY!!!!")


def prepare(bot: commands.Bot):
    bot.add_cog(Responder(bot))
    bot.add_cog(Responder2(bot))
