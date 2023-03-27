# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands
from db.db_operations import zvute_random_choice_username

import logging
import random

logger = logging.getLogger(__name__)

#
# Command inspired by @B3art
#

class ZvuTe(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def zvute(self, ctx: commands.Context):
        list_users = await zvute_random_choice_username()

        if self.bot.nick in list_users:
            list_users.remove(self.bot.nick)

        list_users.remove(ctx.author.name)

        if len(list_users) > 0:
            rnd = random.choice(list_users)
            await ctx.send(f"@{ctx.author.name} pozval na virtualni kavu chatujici @{rnd}")

def prepare(bot: commands.Bot):
    bot.add_cog(ZvuTe(bot))
