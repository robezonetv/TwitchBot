# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

import logging
import time
from typing import List, Union

from asgiref.sync import sync_to_async

from db.models import TwitchUsers
from db.models import User

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
        logger.info(f"Updating message count for user {name}")
    except TwitchUsers.DoesNotExist:
        # TODO udelat specialni request na Twitch a ziskat jeho Twitch ID
        await TwitchUsers.objects.acreate(
            username=name,
            msg_count=1,
            last_msg_timestamp=msg_time,
            # twitch_id=random.randint(1, 1000000), ## testing
        )
        logger.info(f"Adding user to database {name} and update 'msg_count'")


async def get_active_users_in_last_5_minutes() -> Union[List[str], None]:
    time_range = int(time.time() - 300)
    active_users = []
    async for username in TwitchUsers.objects.filter(last_msg_timestamp__gt=time_range):
        active_users.append(username.username)
    logger.info(f"Active users in last 5 minutes: {active_users}")
    return active_users
