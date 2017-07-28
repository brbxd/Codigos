# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:11:29 2017

@author: Bruno Rigueti
"""
# Insercao dos dados:

a = input('insert a number: ')
b = input('insert a number: ')

# Definição da Funcao:
    
def mmc(a, b):
    # Variaveis da Funcao:
    
    a = int(a)
    b = int(b)
    x = []
    p = [2, 3, 5, 7, 11, 13, 17]
    
    # Calculos da Funcao:
    
    while a > 1 or b > 1:
         for i in p:
             if a % i == 0 or b % i == 0:
                 x.append(i)
                 if a % i == 0:
                     a /= i
                 if b % i == 0:
                     b /= i
    n = 1
    for j in x:
        n *= j
    return n
    
# Invocando a Funcao:

y = mmc(a, b)
print(y)