# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:54:57 2015

@author: elsa
"""


def mul(list):
    if len(list) == 0:
        return 0
    else:
        a = 1
        for number in list:
            a = number * a
    return a


'''
def mul(list):
    if len(list) == 0:
        return 0   #if I put a==0 instead of the return, nothing stops Python
                    from doing the else#
    if len(list) == 1:
        a = list[0]
    else:
        a = list[0]
        for i in range(1, len(list)):
            a = operator.mul(list[i], a)
    return a
'''
