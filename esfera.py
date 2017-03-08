# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:08:48 2017

@author: alumno
"""

from random import *
from pylab import *
from math import *

N=10000000
cuenta=0
f=[]

for i in range(N):
    x=random()
    y=random()
    z=random()
    
    if x**2+y**2+z**2<1:
        cuenta=cuenta+1
    
    if i%100:
        f.append(cuenta)
        
hist(f, bins=100)     
    
print(8*cuenta/N)