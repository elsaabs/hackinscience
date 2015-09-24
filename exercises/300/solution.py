# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:56:55 2015

@author: elsa
"""

doc = open('words.txt')
list = [line.split(',') for line in doc.readlines()]
for i in range(0, len(list)):
    print(''.join(list[i]).rstrip('\n'))
