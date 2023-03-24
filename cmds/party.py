# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands

class party(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def party(self, ctx: commands.Context):
        await ctx.send(f"EEEEEEEJ PARTY!!!!")

def prepare(bot: Bot):
    bot.add_cog(party(bot))
