# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:37:07 2015

@author: elsa
"""


def love_meet(l1, l2):
    return set(l1).intersection(l2)


def affair_meet(l1, l2, l3):
    return set(l2).intersection(l3) - set(l1).intersection(l2)
