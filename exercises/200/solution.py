# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:29:21 2015

@author: elsa
"""


def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
