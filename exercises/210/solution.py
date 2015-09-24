# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:17:24 2015

@author: elsa
"""

import is_prime
prime1000 = []
for i in range(1, 1000):
    if is_prime.is_prime(i):
        prime1000.append(i)
print(sum(prime1000))
