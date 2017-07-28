# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 20:44:28 2017

@author: Bruno Rigueti
"""

x = [1, 2, 3, 4, 5, 6]

def max(arr):
    arr.sort()
    a = arr[::-1]
    c = a[0]
    return c
    
def min(arr):
    arr.sort()
    b = arr[0]
    return b
print(max(x))
print(min(x))