# -*- encoding: utf-8 -*-
# ! python3

from twitchio.ext import commands

class SocialLinks(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def gist(self, ctx: commands.Context):
        await ctx.send(f"Moje gisty najdes tu: https://gist.github.com/robezonetv")

    @commands.command(aliases=['socials'])
    async def social(self, ctx: commands.Context):
        await ctx.send(f"DISCORD::https://discord.com/invite/bjcYu3BR68 INSTAGRAM::https://www.instagram.com/robezonetv TWITTER::https://twitter.com/robezonetv GITHUB::https://github.com/robezonetv")

    @commands.command(aliases=['ig'])
    async def instagram(self, ctx: commands.Context):
        await ctx.send(f"Instagram je tady: https://instagram.com/robezonetv :)")

    @commands.command(aliases=['dc'])
    async def discord(self, ctx: commands.Context):
        await ctx.send(f"Discord najdes tady: https://discord.com/invite/bjcYu3BR68 --> Ziskas tim lepsi notifikace --> Muzes nominovat temata --> Muzes se na cokoliv zeptat --> Jsme ve spojeni i mimo stream :)")

    @commands.command(aliases=['free','xmas'])
    async def server(self, ctx: commands.Context):
        await ctx.send(f"Nikdo ti dnes neda nic zadarmo, a ja si rekl NE! Dam ti server zadarmo a to hned. Jdi na https://valheim.robe.zone a tam si zaloz Valheim server zcela zdarma. :)")

def prepare(bot: commands.Bot):
    bot.add_cog(SocialLinks(bot))
