# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:37:35 2015

@author: elsa
"""


def select_student(my_class, min):
    accepted = []
    refused = []
    for student in my_class:
        if student[1] > min:
            accepted.append(student)
        else:
            refused.append(student)
    return {'Accepted': accepted, 'Refused': refused}
