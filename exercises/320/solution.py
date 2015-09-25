# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:56:46 2015

@author: elsa
"""

with open('words.txt', encoding="utf-8") as doc:
    content = doc.read()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        print(letter, ': ', round(content.count(letter) / len(content), 2),
              sep='')

'''
unnecessary DOUBLE BOUCLE
with open('words.txt', encoding="utf-8") as doc:
    content = doc.read()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    j = []
    for letter in alphabet:
        print(letter, ':', content.count(letter))
        j.append(content.count(letter))
    print(j)
    total = (sum(j))
    for letter in alphabet:
        print(letter, ':', round(content.count(letter) / total, 2))
'''
