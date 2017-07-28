# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 18:44:02 2016

@author: Bruno Rigueti
"""
#Imprime os numeros pares de 0 a 50:
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

# Elemento i: item na lista
# for i in range(51): conjunto de itens a serem considerados para serem incluídos na lista
# if i % 2 == 0: condição para o item ser incluído na lista

# Exemplo de uma lista contendo os quadrados pares dos números de 1 a 11:
even_squares = [x ** 2 for x in range(1, 11) if (x ** 2) % 2 == 0]
print(even_squares)

# Exemplo de uma lista contendo os cubos dos números de 1 a 10 que são divisíveis por 4:
cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
print(cubes_by_four)