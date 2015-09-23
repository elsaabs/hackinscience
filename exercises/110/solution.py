# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:26:15 2015

@author: elsa
"""

import sys

if sys.argv[2] == "+":
    print(int(sys.argv[1]) + int(sys.argv[3]))
if sys.argv[2] == "-":
    print(int(sys.argv[1]) - int(sys.argv[3]))
if sys.argv[2] == "/":
    print(int(sys.argv[1]) / int(sys.argv[3]))
if sys.argv[2] == "\*":
    print(int(sys.argv[1]) * int(sys.argv[3]))
if sys.argv[2] == "^":
    print(int(sys.argv[1]) ** int(sys.argv[3]))
if sys.argv[2] == "%":
    print(int(sys.argv[1]) % int(sys.argv[3]))
