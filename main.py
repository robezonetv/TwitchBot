############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """
import logging

# Turn off bytecode generation
import sys

from utils.log import load_logging
from utils.utils import reloader

sys.dont_write_bytecode = True
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django

django.setup()
# Import your models for use in your script

from db.db_operations import add_user, increase_user_msg_count, zvute_random_choice_username
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()
load_logging()
logger = logging.getLogger(__name__)

####################################################
#               START OF APPLICATION               #
####################################################
""" Replace the code below with your own """


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=os.environ["ACCESS_TOKEN"],
            prefix="!",
            initial_channels=[os.environ["CHANNEL_NAME"]],
        )

    async def event_ready(self):
        logger.info(f"User id is | {self.user_id}")
        self.reload_modules()
        await self.connected_channels[0].send("I'm ready v2!")

    async def event_message(self, message):
        await increase_user_msg_count(message.author.name)
        await self.handle_commands(message)

    @commands.command()
    async def reload(self, ctx: commands.Context):
        self.reload_modules()
        await add_user(ctx.author.name)
        await ctx.send(f"All modules reloaded!")

    def reload_modules(self):
        reloader(self)


if __name__ == "__main__":

    bot = Bot()
    bot.run()
