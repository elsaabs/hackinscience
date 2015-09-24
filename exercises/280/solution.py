# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:26:15 2015

@author: elsa
"""
import sys

try:
    print(sys.argv[1])
except IndexError:
    print('Not enough parameters.')
