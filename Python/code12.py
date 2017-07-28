# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [0, 0, 0, 0, 0, 0, 0]
for i in x:
    y[i - 1] = -4 * i + 1,5
    i = i + 1

plt.plot(y, 'k-D')
    
