# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

from twitchio.ext import commands


class party(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def party(self, ctx: commands.Context):
        await ctx.send(f"EEEEEEEJ PARTY!!!!")
        #await ctx.send(f"HA!")

    # @commands.Cog.event()
    # async def event_message(self, message):
    #     # An event inside a cog!
    #     if message.echo:
    #         return
    #
    #     print(message.content)


#def prepare_responder(bot: commands.Bot):
#    bot.add_cog(SimpleResponses(bot))
#    bot.add_cog(SimpleResponses(bot))
#    print("Responder is ready")

def prepare(bot: Bot):
    bot.add_cog(party(bot))
