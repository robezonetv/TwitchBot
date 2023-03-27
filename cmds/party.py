# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands, sounds

import logging
import os

logger = logging.getLogger(__name__)

class Party(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def party(self, ctx: commands.Context):
        # BUG in pyaudio
        # sound = sounds.Sound(source='party.mp3')
        # self.bot.player.play(sound)
        await ctx.send(f"Dance Dance Dance")

def prepare(bot: commands.Bot):
    bot.add_cog(Party(bot))
