# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 23:01:25 2016

@author: Bruno Rigueti
"""
#Codigo para verificar se um número é primo:
    
def is_prime(x):
    if x < 2:
        return False
    else:
        n = 2
        while n < x:
            if x % n == 0:
                return False
                break
            n += 1
        else:
            return True

y = int(input('enter a number: '))

z = is_prime(y)

if z == True:
    z = 'Yes'
else:
    z = 'No'
print('')
print ('Is it a prime? A. ' + z)