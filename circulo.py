# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:31:51 2017

@author: alumno
"""
from pylab import *
from random import random
N=195000000
cuenta=0

p=[]
o=[]
for i in range (N):
    x=random()
    y=random()
    
    if x**2+y**2<1:
        cuenta=cuenta+1
        
    if i%10000==0 and i>0:
        print(i,4*cuenta/i)
        p.append(i)
        o.append(4*cuenta/i)
        
print(4*cuenta/N)
plot(p,o)
show()