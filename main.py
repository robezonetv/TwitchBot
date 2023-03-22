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
from cogs.responder import prepare_responder


load_dotenv()


####################################################
#               START OF APPLICATION               #
####################################################
""" Replace the code below with your own """


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=os.environ["ACCESS_TOKEN"], prefix='!', initial_channels=['...'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

        prepare_responder(self)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await add_user(ctx.author.name)
        await ctx.send(f"Hello, {ctx.author.name}!")


if __name__ == '__main__':
    bot = Bot()
    bot.run()
