# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 22:28:53 2017

@author: Bruno Rigueti
"""

# O código converte um array de sinais binarios em um numero inteiro:

def binary_array_to_number(arr):
    a = ''
    for i in arr:
        i = str(i)
        a += i
    b = int(a, 2)
    return b
a = [1, 1, 1, 1, 1] # retorna 31
b = binary_array_to_number(a)
print(b)