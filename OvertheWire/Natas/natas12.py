#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright 2020 leaundre leaundre.jackson87@gmail.com
#
# Distributed under terms of the %LICENSE% license.

"""
A script to use in Natas Wargame room in OvertheWire
"""

from urllib.parse import unquote
import re
import base64
import requests

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth=(username, password))

content = response.text
print(content)
