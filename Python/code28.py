# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 17:53:37 2016

@author: Bruno Rigueti
"""
# Exemplo de um dictionary simples:
my_dict = {"a": 2, "b": 4, "c": 6}

# Imprime os pares Key:Value do dictionary em uma lista:
print(my_dict.items())

# Imprime as Keys do dictionary:
print(my_dict.keys())

# Imprime os Values do dictionary:
print(my_dict.values())

# Imprime um par Key:Value por linha:
for i in my_dict:
    print(i, my_dict[i])