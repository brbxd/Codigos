# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:37:23 2017

@author: Bruno Rigueti
"""
# O codigo calcula a persistencia da soma de um numero - quantas 
# vezes seus digitos se somam um pelo outro até se tornar um valor de 
# apenas 1 digito.

def persistencex(n):
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
                a += j
            n = a
    else:
        p = 0
    return p