# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:10:14 2015

@author: elsa
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(0, 26):
    for j in range(0, 26):
        if i != j:
            print(alphabet[i] + alphabet[j])
