# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
from seaborn import plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [0]

for i in x:
    y.append((i ** 2) + (3 * i) + 1)
    
print(y)

plt.plot(y)