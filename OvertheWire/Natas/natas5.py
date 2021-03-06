#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2020 leaundre leaundre.jackson87@gmail.com
#
# Distributed under terms of the %LICENSE% license.

"""
A script to use in Natas Wargame room in OvertheWire
"""

import re
import requests

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

# headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
cookies = {"loggedin": "1"}

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

response = session.get(url, auth=(username, password), cookies=cookies)
content = response.text

# print(content)
# print(session.cookies)
print(re.findall(' natas6 is (.*)</div>', content)[0])
