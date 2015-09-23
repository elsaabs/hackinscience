# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:26:15 2015

@author: elsa
"""

import sys
import operator
operators = {'+': operator.add, '-': operator.sub, '/': operator.truediv,
             '\*': operator.mul, '^': operator.pow, '%': operator.mod}
if len(sys.argv) == 4:
    try:
        print(operators[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3])))
    except (ValueError, ZeroDivisionError, KeyError):
        print('input error')
else:
    print('usage: ./solution.py a_number (an_operator +-*/%^) a_number')
