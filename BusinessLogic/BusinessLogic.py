# Internal business logic example
# Copyright (C) 2019  Alex Milman

import ConfigParser
from ScrapingUtils import SteamScrapingUtils

config = ConfigParser.ConfigParser()
config.read('application.config')


def test():
    SteamScrapingUtils.get_steam_user_name_from_steam_id('76561198018110309')
    SteamScrapingUtils.get_game_data_example('Conarium', 'https://store.steampowered.com/app/313780/Conarium/')



