# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands
from db.db_operations import zvute_random_choice_username
import logging

logger = logging.getLogger(__name__)

class ZvuTe(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def zvute(self, ctx: commands.Context):
        list_users = await zvute_random_choice_username()
        logger.info(f"{list_users}")
        await ctx.send(f"Pozvani v2")


def prepare(bot: commands.Bot):
    bot.add_cog(ZvuTe(bot))
