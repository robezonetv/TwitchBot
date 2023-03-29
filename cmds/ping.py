# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"pong")


def prepare(bot: commands.Bot):
    bot.add_cog(Ping(bot))
