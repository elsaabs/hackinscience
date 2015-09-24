# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:48:41 2015

@author: elsa
"""

import is_prime
for i in range(222281, 222381):
    if is_prime.is_prime(sum([int(x) for x in bin(i).lstrip('0b')])):
        print(i)
