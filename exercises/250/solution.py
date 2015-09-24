# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:31:22 2015

@author: elsa
"""


def draw_n_squares(n):
    draw = []
    for i in range(0, n):
        draw.append('+---'*n + '+')
        draw.append('|   '*n + '|')
    draw.append('+---'*n + '+')
    return '\n'.join(str(item) for item in draw)

'''
TO CHECK IN THE TERMINAL WHAT'S THE PROBLEM:
import sys

print(draw_n_squares(int(sys.argv[1])))
'''
