# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 20:54:59 2016

@author: Bruno Rigueti
"""
x = 1
i = 2
z = [0]
y = [0]

while x < 11:
    z = list(range(x))    
    z[x - 1] = x    
    x = x + 1
  
for i in z:
    y = list(range(i))
    y[i - 1] = 2 * i
    i = i + 1

print(z)
print(y)