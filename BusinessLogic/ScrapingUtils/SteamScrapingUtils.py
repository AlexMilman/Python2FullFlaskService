# Steam scraping examples
# Copyright (C) 2019 Alex Milman

from BusinessLogic.ScrapingUtils import SteamConsts
from BusinessLogic.Utils import WebUtils, StringUtils, LogUtils



def get_steam_user_name_from_steam_id(user_id):
    html_content = WebUtils.get_html_page(SteamConsts.STEAM_PROFILE_LINK + user_id)
    steam_user_name = WebUtils.get_item_by_xpath(html_content, u'.//span[@class="actual_persona_name"]/text()')
    return steam_user_name


def get_game_data_example(game_name, game_link):
    LogUtils.log_info('Processing game ' + game_name)
    steam_score = 0
    num_of_reviews = 0
    html_content = WebUtils.get_html_page(game_link, "birthtime=-7199; lastagecheckage=1-January-1970; mature_content=1;")
    base_game_link = WebUtils.get_item_by_xpath(html_content, u'.//div[@class="glance_details"]/a/@href')
    if base_game_link is not None:
        # If this is DLC - get additional data according to base game
        html_content = WebUtils.get_html_page(base_game_link, "birthtime=-7199; lastagecheckage=1-January-1970; mature_content=1;")
    steam_game_tooltip = WebUtils.get_items_by_xpath(html_content, u'.//div[@class="user_reviews_summary_row"]/@data-tooltip-html')[-1]
    if steam_game_tooltip != 'Need more user reviews to generate a score' and steam_game_tooltip != 'No user reviews':
        steam_score = StringUtils.normalize_int(steam_game_tooltip.split('%')[0])
        num_of_reviews = StringUtils.normalize_int(steam_game_tooltip.split('of the')[1].split('user reviews')[0])
    return steam_score, num_of_reviews


def get_games_from_package(package_name, package_link):
    LogUtils.log_info('Processing package ' + package_name)
    html_content = WebUtils.get_html_page(package_link, "birthtime=-7199; lastagecheckage=1-January-1970; mature_content=1;")
    games = WebUtils.get_items_by_xpath(html_content, u'.//a[@class="tab_item_overlay"]/@href')
    return games


