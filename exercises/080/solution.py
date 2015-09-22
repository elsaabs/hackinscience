# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:15:37 2015

@author: elsa
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(0, 26):
    for j in range(i+1, 26):
            print(alphabet[i] + alphabet[j])
