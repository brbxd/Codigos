# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:16:46 2016

@author: Bruno Rigueti
"""

import numpy
import statistics as st

x = [0]
y = [0]
i = 1
k = input("Insert Range:")
m = int(k)

while i < m:
    x = list(range(i))
    x[i - 1] = i
    i = i + 1
    
z = len(x)
j = int(z)

y = list(range(j))

y = (numpy.multiply(x, 2)) + 3

w1 = st.mean(x)
w2 = st.mean(y)

w3 = st.stdev(x)
w4 = st.stdev(y)

print(x)
print(list(y))
print("---------------------------------------------")
print(w1)
print(w2)
print("---------------------------------------------")
print(w3)
print(w4)