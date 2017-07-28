# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 19:36:46 2016

@author: Bruno Rigueti
"""

# Para passar uma função que selecona itens de uma lista de acordo com um critério:
squares = [x ** 2 for x in range(1, 11)]
x = filter(lambda x: x >= 30 and x <= 70, squares)
print(x)