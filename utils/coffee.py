# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

import math
from typing import Union

from twitchio.ext import commands


def parse_coffee_amount_from_kav_command(ctx: commands.Context) -> Union[int, None]:
    try:
        amount = ctx.message.content.split(" ")[1]
    except IndexError:
        return None

    if not amount.isnumeric():
        return None

    return int(amount)


def amount_to_coffees(amount: int):

    return math.ceil(amount * 0.042 / 5)
