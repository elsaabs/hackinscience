# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:03:31 2015

@author: elsa
"""

doc = open('words.txt', encoding="utf-8")
list = [line.split(',') for line in doc.readlines()]
nbre = []
for i in range(0, len(list)):
    text = ''.join(list[i]).rstrip('\n')
    nbre.append(text.count('e'))
print(sum(nbre))
