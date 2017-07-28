# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 22:19:54 2017

@author: Bruno Rigueti
"""

# Codigo para contar itens em um array:

def count_sheeps(arrayOfSheeps):
  a = 0
  for i in arrayOfSheeps:
      if i == True:
          a += 1
  return a
a = [True, True, False, True]
b = count_sheeps(a)
print(b)