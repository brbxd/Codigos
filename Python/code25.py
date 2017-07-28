# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 21:57:59 2016

@author: Bruno Rigueti
"""
#Função para Calcular a Soma dos dígitos de um número:

def digit_sum(n):
    n = str(n)
    x = []
    for i in n:
        i = int(i)
        x.append(i)
    return sum(x)
y = int(input('enter a number: '))
print("")
print('Digits Sum = ' + str(digit_sum(y)))