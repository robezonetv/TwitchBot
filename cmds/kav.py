# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands

class kav(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def kav(self, ctx: commands.Context):
        await ctx.send(f"XYZ CZK je 16.91 virtualnich kav.")
        #await ctx.send(f"HA!")

def prepare(bot: Bot):
    bot.add_cog(kav(bot))
