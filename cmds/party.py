# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands


class Party(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def party(self, ctx: commands.Context):
        await ctx.send(f"EEEEEEEJ PARTY!!!!")


def prepare(bot: commands.Bot):
    bot.add_cog(Party(bot))
