# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:12:17 2015

@author: elsa
"""
import math
import numpy as np


def euclidean(a, b):
    return ((b[0]-a[0]) ** 2 + (b[1]-a[1]) ** 2) ** 0.5


def opt_euclidean(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    return math.hypot(x, y)


def np_euclidean(a, b):
    return np.sqrt(np.power(np.array(a) - np.array(b), 2))
