# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

import logging
import time

from django.db.models import F
from asgiref.sync import sync_to_async

from db.models import User
from db.models import TwitchUsers

logger = logging.getLogger(__name__)

async def add_user(name):
    logger.info(f"Adding user {name}")
    await User.objects.acreate(name=name)

async def increase_user_msg_count(name: str) -> None:
    msg_time = int(time.time())
    try:
        obj = await TwitchUsers.objects.aget(username=name)
        obj.msg_count += 1
        obj.last_msg_timestamp = msg_time
        await sync_to_async(obj.save)()
        logger.info(f"Updating 'msg_count' for user {name}")
    except TwitchUsers.DoesNotExist:
        #TODO udelat specialni request na Twitch a ziskat jeho Twitch ID
        await TwitchUsers.objects.acreate(
            username=name, msg_count=1, last_msg_timestamp=msg_time
        )
        logger.info(f"Adding user to database {name} and update 'msg_count'")

async def zvute_random_choice_username():
    logger.info(f"Random choose username from chatter for !zvute")
    time_range=int(time.time() - 300)
    results = []
    async for username in TwitchUsers.objects.filter(last_msg_timestamp__gt=time_range):
        results.append(username.username)
    return results
