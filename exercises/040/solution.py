# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:24:00 2015

@author: elsa
"""

even = []
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
print(sum(even))
