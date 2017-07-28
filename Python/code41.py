# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:39:41 2017

@author: Bruno Rigueti
"""

# O codigo mede a razao entre a persistencia e a persistencia da soma de um
# numero.

from code39 import persistence
from code40 import persistencex

a = int(input('insert a number: '))
b = persistence(a)
c = persistencex(a)
d = b / c
print(d)