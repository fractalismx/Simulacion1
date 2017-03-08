# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:06:47 2017

@author: alumno
"""

from random import *
from pylab import *
from math import *

#Parametros
sigma=0.02
mu=0.01
#valores iniciales
s0=10
s10=[]
s15=[]
suma=0
k=0
#valor de interes
T=10
#numero de repeticiones
m=10000
n=15
#crear lista
l=[]
b=[]
x=0
h=0.02

"""
while x<0.9:
    b.append(x)
    x=x+h
for i in range(m):
    #s0=s0*exp(T*mu+sqrt(T)*gauss(0,sqrt(T)))
    
    if s>k:
        suma=suma+(s0-k)    
    else:
        l.append(0)
print(suma/m)
hist(2,bins=b,color='red')
"""

for i in range (m):
    aux=s0

    for i in range(0,n):
        
        s0=s0*exp(mu+sigma*gauss(0,1))
        
        if i == 10:
            s10.append(s0)
        
    s15.append(s0)
    
    s0=aux    

m15=0
m10=0

for i in range(m):
    
    m15=s15[i]+m15

m15=m15/m

print(m15)    

for i in range(m):
    
    m10=s10[i]+m10

m10=m10/m

print(m10) 