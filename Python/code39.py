# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:18:48 2017

@author: Bruno Rigueti
"""
# O codigo calcula a persistencia de um numero - quantas vezes seus digitos
# se multiplicam um pelo outro até se tornar um valor de apenas 1 digito.

def persistence(n):
    if n > 9:
        p = 0
        while n > 9:            
            p += 1
            n = str(n)
            x = []
            a = 1
            for i in n:
                i = int(i)
                x.append(i)            
            for j in x:
                a *= j
            n = a
    else:
        p = 0
    return p