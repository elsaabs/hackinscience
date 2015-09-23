# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:25:18 2015

@author: elsa
"""


def perfect_shuffle(deck):
    j = []
    m = int(len(deck)/2)
    if len(deck) % 2 == 0:
        l1 = deck[: m]
        l2 = deck[m:]
        for i in range(0, len(deck[: m])):
            j.append(l1[i])
            j.append(l2[i])
        return j
    else:
        l1 = deck[: m + 1]
        l2 = deck[1 + m:]
        for i in range(0, m):
            j.append(l1[i])
            j.append(l2[i])
        j.append(l1[m])
        return j
