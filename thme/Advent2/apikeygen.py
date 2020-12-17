#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright %YEAR% %USER% <%MAIL%>
#
# Distributed under terms of the %LICENSE% license.

import requests

for api_key in range(1, 100, 2):
    print(f"api_key {api_key}")
    html = requests.get(f'http://10.10.72.1:8000/api/{api_key}')
    print(html.text)
