# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:31:14 2016

@author: Bruno Rigueti
"""
print("Análise do Triângulo Retângulo")
print("-------------------------------------------------")
b = input('Cateto Maior: ')
c = input('Cateto Menor: ')

b = float(b)
c = float(c)

def cat1(b):
    return b ** 2
    
def cat2(c):
    return c ** 2
    
def hyp(b, c):
    x = cat1(b)
    y = cat2(c)
    z = x + y
    return z ** 0.5
    
print("-------------------------------------------------")
a = hyp(b, c)
print("Hipotenusa: "+str(a))
print("-------------------------------------------------")
h = a + b + c
print("Perímetro: "+str(h))
print("-------------------------------------------------")
p = (b * c) / 2
print("Área: "+str(p))
print("-------------------------------------------------")