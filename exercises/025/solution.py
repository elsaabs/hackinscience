# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:22:26 2015

@author: elsa
"""

from datetime import date
from time import gmtime, strftime
d = date.today()
print('Today is', d.isoformat(), 'and it is', strftime("%H:%M:%S", gmtime()))
