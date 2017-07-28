# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:22:35 2017

@author: Bruno Rigueti
"""
# O Codigo teste se um triangulo pode ser formado com as dimensoes informadas:

def is_triangle(a, b, c):
    x = a + b
    y = a + c
    z = b + c
    if c >= x or b >= y or a >= z:
        return False
    else:
        return True
a = input('dimension 1: ')
b = input('dimension 2: ')
c = input('dimension 3: ')
n = is_triangle(a, b, c)
print(n)
