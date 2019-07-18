# Utilities for working with strings
# Copyright (C) 2019 Alex Milman


import hashlib


def normalize_int(int_str):
    return int(int_str.replace(',', ''))


def get_hashed_id(string):
    return hashlib.md5(string).hexdigest()