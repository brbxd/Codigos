# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:56:16 2016

@author: Bruno Rigueti
"""
# Par ordenado - algoritmo 3:

v1 = input('enter the range: ')
v2 = input('enter the power: ')

r = int(v1)
p = int(v2)

x = []
y = []

for i in range(r):
    x.append(i)
    
for j in x:
    y.append(j ** p)
    
from statistics import mean

print("")
print('x = ' + str(x))
a = mean(x)
print('avg(x) = ' + str(a))
print("")
print('y = ' + str(y))
b = mean(y)
print('avg(y) = ' + str(b))
print("")
print('avg div: ' + str(b / a))