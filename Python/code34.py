# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 20:22:05 2017

@author: Bruno Rigueti
"""
# O código abaixo separa os 2 maiores dígitos de uma string que 
# contenha só números

num = input("insert a number string: ")
def high_and_low(numbers):
    # Exclui os espacos:
    n = [int(s) for s in numbers.split(" ")]
    # Separa o max e o min e converte em string:
    return "%i %i" % (max(n), min(n))
a = high_and_low(num)
print(a)