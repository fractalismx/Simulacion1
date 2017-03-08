# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:08:48 2017

@author: alumno
"""

from random import *
from pylab import *
from math import *
m=1000
N=10000

f=[]
for k in range(m):
    cuenta=0
    for i in range(N):
        x=random()
        y=random()
        z=random()
        
        if x**2+y**2+z**2<1:
            cuenta=cuenta+1
    f.append(8*cuenta/N)
    
f.sort()
q=len(f)

li=f[int(0.05*q)]
ld=f[int(0.95*q)]

print(li,ld)   

sigma=0

for j in range(q):
    sigma=sigma+(mu-f[j])**2
  
sigma=sigma/N
sigma=sqrt(sigma)

limite_inferior=mu-1.65*sigma
limite_superior=mu+1.65*sigma

print(limite_inferior)
print(limite_superior)

print(mu)
print(q)