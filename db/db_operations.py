# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

import logging
import time

from django.db.models import F
from django.utils.functional import async_to_sync

from db.models import User
from db.models import TwitchUsers

logger = logging.getLogger(__name__)

async def add_user(name):
    logger.info(f"Adding user {name}")
    await User.objects.acreate(name=name)

async def increase_user_msg_count(name):
    logger.info(f"Adding user {name}")
    msg_time=int(time.time())
    await TwitchUsers.objects.aupdate_or_create(username=name)
    await TwitchUsers.objects.filter(username=name).aupdate(msg_count=F("msg_count") + 1, last_msg_timestamp=msg_time)

async def zvute_random_choice_username():
    logger.info(f"Random choose username from chatter for !zvute")
    time_range=int(time.time() - 300)
    queryset = TwitchUsers.objects.filter(last_msg_timestamp__gt=time_range)
    filtered_data = await async_to_sync(queryset)
    return filtered_data
