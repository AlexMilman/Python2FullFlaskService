# MySql connector example
# Copyright (C) 2019  Alex Milman

import pymysql
import ConfigParser

import time

from BusinessLogic.Utils import StringUtils, LogUtils

config = ConfigParser.ConfigParser()
config.read('application.config')
host = config.get('MySql', 'Host')
port = int(config.get('MySql', 'Port'))
user = config.get('MySql', 'User')
password = config.get('MySql', 'Password')
db_schema = config.get('MySql', 'DBSchema')


def insert_example(group_name, group_webpage, cookies):
    connection = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db_schema, charset='utf8')
    cursor = connection.cursor()

    cursor.execute('INSERT IGNORE INTO Groups (GroupID,Users,Giveaways,Name,Webpage,Cookies) '
                   'VALUES ("' + StringUtils.get_hashed_id(group_webpage) + '","[]","[]","' + group_name + '","' + group_webpage + '","' + to_str(cookies.replace('"','')) + '")')

    connection.commit()  # you need to call commit() method to save your changes to the database

    cursor.close()
    connection.close()


def fetch_example():
    start_time = time.time()
    connection = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db_schema, charset='utf8')
    cursor = connection.cursor()

    groups = dict()
    cursor.execute("SELECT Name,Webpage FROM Groups WHERE Users='[]' AND Giveaways='[]'")
    data = cursor.fetchall()
    for row in data:
        groups[row[0]] = row[1]

    cursor.close()
    connection.close()

    LogUtils.log_info('Get all empty groups took ' + str(time.time() - start_time) + ' seconds')
    return groups


def to_str(param):
    if not param:
        return ''
    return str(param)