# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 21:42:08 2016

@author: Bruno Rigueti
"""
#Função para Calcular o Fatorial(n!) de um número:

def factorial(x):
    y = []
    for i in range(1, x + 1):
        y.append(i)
    w = 1
    for j in y:
        w = w * j
        j = j + 1
    return w
n = int(input('enter a number: '))
print(" ")
print ('Factorial = ' + str(factorial(n)))