# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:34:56 2015

@author: elsa
"""
import mul


def euler(list):
    j = []
    for i in range(13, len(list)):
        a = mul.mul(list[i - 13: i])
        j.append(a)
    return max(j)

'''
MULTIPLY 4 NUMBERS:
import mul


def euler(list):
    j = []
    for i in range(5, len(list)):
        print("i: {}".format(i))
        print("list[i-5]: {}, list[i-4]: {}, list[i-3]: {}, list[i-2]: {},\
               list[i-1]: {}, list[i]: {}".format(list[i - 5], list[i - 4],
                                                  list[i - 3], list[i - 2],
                                                  list[i - 1], list[i]))
        a = mul.mul(list[i - 5: i])
        print("a: {}".format(a))
        j.append(a)
        print("j: {}".format(j))
    return max(j)
'''

'''
MULTIPLY 2 NUMBERS:
import mul


def euler(list):
    j = []
    for i in range(1, len(list)):
        print("i: {}".format(i))
        print("list[i-1]: {} and list[i]: {}".format(list[i - 1], list[i]))
        a = mul.mul(list[i - 1: i + 1])
        print("a: {}".format(a))
        j.append(a)
        print("j: {}".format(j))
    return max(j)
'''
