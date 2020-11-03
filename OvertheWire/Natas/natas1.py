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

username = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto' 

url = 'http://%s.natas.labs.overthewire.org/' % username

reponse = requests.get(url, auth=(username, password))
content = reponse.text

print(re.findall('<!--The password for natas2 is (.*) -->', content)[0])
