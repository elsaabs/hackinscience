# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:57:49 2015

@author: elsa
"""
from euler import euler

with open('1000digit.txt', encoding="utf-8") as doc:
    digit = doc.read().replace('\n', '')
    digitlist = list([int(x) for x in digit])
    print(euler(digitlist))
