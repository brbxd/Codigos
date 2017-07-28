# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:25:58 2016

@author: Bruno Rigueti
"""

def div(x, y):
    if y > 0:
        return x / y
    else:
        return "You can't divide by 0"

x = float(input("Insert a number: "))
y = float(input("Insert a number: "))

z = div(x, y)

print('________________')
print(round(z, 2))