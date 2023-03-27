# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands

class Offers(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def rpishop(self, ctx: commands.Context):
        await ctx.send(f"Sleva 15 Kc na prvni nakup na RPishop.cz. Zaroven rozsiris moznosti tohoto streamu o 30 Kc za co ti velmi dekuji! Staci vyuzit tento vernostni odkaz -> https://rpishop.cz/?rid=28756")

def prepare(bot: commands.Bot):
    bot.add_cog(Offers(bot))
