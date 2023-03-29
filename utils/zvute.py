# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

import logging
import random
from typing import Union

from db.db_operations import get_active_users_in_last_5_minutes

logger = logging.getLogger(__name__)


async def zvute_random_choice_username(
    bot_name: str = None, user_name: str = None
) -> Union[str, None]:
    logger.info(f"Random choose username from chatter for !zvute")

    active_users = await get_active_users_in_last_5_minutes()

    if bot_name in active_users and bot_name != user_name:
        active_users.remove(bot_name)
    active_users.remove(user_name)

    if not active_users:
        return None

    coffee_partner = random.choice(active_users)
    logger.info(f"Coffee partner for {user_name} is {coffee_partner}")
    return coffee_partner
