# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:50:19 2015

@author: elsa
"""

multiple = []
for i in range(1, 1000//3+1):
    if 3*i < 1000:
        multiple.append(3*i)
    if (5*i < 1000 and 5*i % 3 != 0):
        multiple.append(5*i)
print(sum(multiple))
