# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

import logging

from db.models import User

logger = logging.getLogger(__name__)


async def add_user(name):
    logger.info(f"Adding user {name}")
    await User.objects.acreate(name=name)
