# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 22:15:40 2016

@author: Bruno Rigueti
"""

def is_prime(x):
    for n in range(2, x):
        if x == 0:
            return False
        else:
            if x % n == 0:
                return False
            else:
                return True
            
y = int(input('enter a number: '))

print(is_prime(y))