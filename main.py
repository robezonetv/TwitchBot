############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """
# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
# Import your models for use in your script

from db.db_operations import add_user
from twitchio.ext import commands
from dotenv import load_dotenv
import glob

load_dotenv()

####################################################
#               START OF APPLICATION               #
####################################################
""" Replace the code below with your own """


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=os.environ["ACCESS_TOKEN"], prefix='!', initial_channels=['robezonetv'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        self.reload_commands()
        await self.connected_channels[0].send('I\'m ready v2!')

    @commands.command()
    async def reload(self, ctx: commands.Context):
        self.reload_commands()
        await add_user(ctx.author.name)
        await ctx.send(f"All modules reloaded!")
    
    def reload_commands(self):
        if not self.cogs:
            cogs = self.get_cmds()
            for cog in cogs:
                self.load_module(cog)
        else:
            cogs = self.get_cmds()
            for cog in cogs:
                cogName=cog.split(".")[1]
                if self.get_cog(cogName) is None:
                    self.load_module(cog)
                else:
                    self.reload_module(cog)

    def get_cmds(self) -> list[str]:
        cmds_files = glob.glob("./cmds/[a-z]*.py")
        return [
            f'cmds.{file.split("/")[2].removesuffix(".py")}'
            for file in cmds_files
            if file.endswith(".py")
        ]

if __name__ == '__main__':
    bot = Bot()
    bot.run()
