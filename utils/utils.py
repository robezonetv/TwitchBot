# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

import fnmatch
import logging
import os
from typing import List

logger = logging.getLogger(__name__)


def module_walk(dir_path: str) -> List[str]:
    """Walks through all modules and returns a list of all module names"""

    module_names = []

    for root, _, files in os.walk(dir_path):  # root, dirs, files
        for filename in fnmatch.filter(files, "*.py"):
            if not filename.startswith("_"):
                module_name = f"{root}.{filename.removesuffix('.py')}"
                module_names.append(module_name)

    return module_names


def reloader(bot, dir_path: str = "cmds") -> None:
    """Reloads all modules in a directory"""

    logger.info(f"Reloading modules...")
    modules = module_walk(dir_path)
    logger.info(f"Actual Modules: {modules}")
    logger.info(f"Pre-reload Cogs: {bot.cogs.keys()}")

    if not bot.cogs:
        for module in modules:
            bot.load_module(module)
    else:
        bot.cogs.clear()  # když se smaže modul a unloadne se, tak se ALE nevymažou cogs - loadem se níže načtou
        for module in modules:
            try:
                bot.unload_module(module)
            except ValueError:
                logger.warning(f"Module {module} not loaded, ignore")
                pass

            bot.load_module(module)
    logger.info(f"After-reload Cogs: {bot.cogs.keys()}")
