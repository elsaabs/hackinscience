# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:17:01 2015

@author: elsa
"""

import is_prime
list = [i for i in range(10000, 10050) if is_prime.is_prime(i)]
print(', '.join(str(item) for item in list))
