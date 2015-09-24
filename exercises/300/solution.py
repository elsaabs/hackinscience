# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:56:55 2015

@author: elsa
"""

import requests
url = "http://julien.palard.fr/x/words"
result = requests.get(url)
print(result.text)
