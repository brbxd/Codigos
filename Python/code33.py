# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:35:40 2017

@author: Bruno Rigueti
"""
# Insercao de Dados:

a = input('insert a number: ')
b = input('insert a number: ')

# Definicao da Funcao:

def mdc(a, b):
    
    # Variaveis da Funcao:
    
    a = int(a)
    b = int(b)
    p = [2, 3, 5, 7, 11, 13, 17]
    x = []
    y = []
    z = []
    
    # Calculos da Funcao:
    
    while a > 1 or b > 1:
        for i in p:
            if a % i == 0:
                x.append(i)
                a /= i
            if b % i == 0:
                y.append(i)
                b /= i
    for i in x:
        if i in y:
            z.append(i)
    print(x)
    print(y)
    print(z)
    n = 1
    for h in z:
        n *= h
    return n
    
# Invocando a Funcao:
r = mdc(a, b)
print(r)
