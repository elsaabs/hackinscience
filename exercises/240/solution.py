# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:10:54 2015

@author: elsa
"""

a, b = 1, 1
fib = []
while b < 90:
    fib.append(b)
    a, b = b, a+b
print(', '.join(str(item) for item in fib))

'''
a, b = 0, 1
fib = []
for len(fib) in range(0, 10):
    fib.append(b)
    a, b = b, a+b
print(fib)
'''
