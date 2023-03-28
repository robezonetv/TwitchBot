# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands

from utils.messages import (
    VALHEIM_MESSAGE,
    INSTAGRAM_MESSAGE,
    DISCORD_MESSAGE,
    SOCIALS_MESSAGE,
    GIST_MESSAGE,
)


class SocialLinks(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def gist(self, ctx: commands.Context):
        await ctx.send(GIST_MESSAGE)

    @commands.command(aliases=["socials"])
    async def social(self, ctx: commands.Context):
        await ctx.send(SOCIALS_MESSAGE)

    @commands.command(aliases=["ig"])
    async def instagram(self, ctx: commands.Context):
        await ctx.send(INSTAGRAM_MESSAGE)

    @commands.command(aliases=["dc"])
    async def discord(self, ctx: commands.Context):
        await ctx.send(DISCORD_MESSAGE)

    @commands.command(aliases=["free", "xmas"])
    async def server(self, ctx: commands.Context):
        await ctx.send(VALHEIM_MESSAGE)


def prepare(bot: commands.Bot):
    bot.add_cog(SocialLinks(bot))
