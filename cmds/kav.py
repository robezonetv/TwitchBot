# -*- encoding: utf-8 -*-
# ! python3

import logging

from twitchio.ext import commands

from utils.coffee import parse_coffee_amount_from_kav_command, amount_to_coffees

logger = logging.getLogger(__name__)


class Kava(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def kav(self, ctx: commands.Context):
        # await ctx.send(f"XYZ CZK je 16.91 virtualnich kav.")
        amount = parse_coffee_amount_from_kav_command(ctx=ctx)
        if not amount:
            await ctx.send(f"!kav <amount>")
            return

        coffees = amount_to_coffees(amount)

        await ctx.send(
            f"{amount} CZK je tady {coffees} ☕️ pro pana medvidka -> !coffee"
        )


def prepare(bot: commands.Bot):
    bot.add_cog(Kava(bot))
