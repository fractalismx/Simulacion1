# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:07:59 2017

@author: alumno
"""

from math import *
from random import *

N=100000

machupichu=0

from i in range(N):
    z=(random()-1)/(2-1)
    
    machupichu=machupichu+sin(z)/z
    
print(machupichu/N)