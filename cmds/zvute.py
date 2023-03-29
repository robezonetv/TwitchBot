# -*- encoding: utf-8 -*-
# ! python3

import logging

from twitchio.ext import commands

from utils.zvute import zvute_random_choice_username

logger = logging.getLogger(__name__)

#
# Command inspired by @B3art
#


class ZvuTe(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def zvute(self, ctx: commands.Context) -> None:
        coffee_partner = await zvute_random_choice_username(
            bot_name=self.bot.nick, user_name=ctx.author.name
        )
        if not coffee_partner:
            await ctx.send(
                f"@{ctx.author.name} zval na virtualni kavu, ale nikdo neodpovedel :("
            )
            return
        await ctx.send(
            f"@{ctx.author.name} pozval na virtualni kavu chatujici @{coffee_partner}"
        )


def prepare(bot: commands.Bot):
    bot.add_cog(ZvuTe(bot))
