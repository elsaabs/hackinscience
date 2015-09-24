# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:45:35 2015

@author: elsa
"""

import requests
try:
    url = "http://mdk.fr/ip"
    result = requests.get(url)
    line = result.text.split('\n')
    print(line[0])
except:
    print("No internet connectivity.")
