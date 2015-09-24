# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:24:33 2015

@author: elsa
"""

from is_prime import is_prime
from itertools import count
for i in count(100000000):
    if is_prime(i):
        print(i)
        break

'''
WORKS!
import is_prime
i = 100000000
while is_prime.is_prime(i) == False:
    i = i + 1
print(i)
'''

'''
TROP LONG
import is_prime
list = [i for i in range(100000000, 1000000000) if is_prime.is_prime(i)]
print(min(list))
'''
