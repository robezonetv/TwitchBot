# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands

from utils.messages import RPI_MESSAGE


class Offers(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def rpishop(self, ctx: commands.Context):
        await ctx.send(RPI_MESSAGE)


def prepare(bot: commands.Bot):
    bot.add_cog(Offers(bot))
