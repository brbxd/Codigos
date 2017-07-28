# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 18:58:38 2016

@author: Bruno Rigueti
"""

# Slice Lists - list[start:end:stride] - start(elemento inicial), end(elemento final), stride(espaço entre eles)
# Start inicia com 0

# Exemplo: Lista:
l = [i ** 2 for i in range(1, 11)]
# Impressão da lista original:
print(l)

# Seleção de números a serem impressos:
print(l[2:9:2])

# Seleção dos últimos números a partir do quarto(indice 3) - por padrão, o último indice é o tamanho da lista:
print(l[3:])

# Seleção até o terceiro número (indice 2 + 1) - por padrão, o primeiro indice é 0, o item final não é incluso:
print(l[:3:])

# Seleção dos números pulando um número - por padrão, o espaço é sempre 1:
# Odd Numbers:
print('Odd = ' + str(l[::2]))

# Even Numbers:
print('Even = ' + str(l[1::2]))

# A Seleção abaixo retorna a lista em ordem inversa (Ex: [a, b] - retorna [b, a]):
print("Inversao = " + str(l[::-1]))

# Posso ainda criar uma nova lista sendo a inversa da anterior, basta atribuir a uma variável:
lr = l[::-1]
print('Nova lista = ' + str(lr))
