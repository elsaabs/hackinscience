# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:57:58 2015

@author: elsa
"""

import sys
import operator
if len(sys.argv) == 3:
    print(operator.add(int(sys.argv[1]), int(sys.argv[2])))
else:
    print('usage: python3 solution.py OP1 OP2')
