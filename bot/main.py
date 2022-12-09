# -*- coding: utf-8 -*-

from nextcord import Intents
from nextcord.ext.commands import Bot

from bot.cogs import register_all_cogs

import toml

config = toml.load('config.toml')

TOKEN = config['discord']['token']
PREFIX = config['discord']['prefix']


def start_bot():
    intents = Intents.default()
    # intents.message_content = True

    bot = Bot(PREFIX, intents=intents)

    register_all_cogs(bot)

    bot.run(TOKEN)
