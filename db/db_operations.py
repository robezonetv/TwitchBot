# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

from db.models import User


async def add_user(name):
    await User.objects.acreate(name=name)
