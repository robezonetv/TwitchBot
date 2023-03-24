# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

import logging


def load_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] [%(name)s:%(module)s - %(funcName)s:%(lineno)s] %(message)s",
    )
