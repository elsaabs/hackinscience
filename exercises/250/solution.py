# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:31:22 2015

@author: elsa
"""


def draw_n_squares(n):
    for i in range(0, n):
        print('+---'*n + '+')
        print('|   '*n + '|')
    print('+---'*n + '+')
