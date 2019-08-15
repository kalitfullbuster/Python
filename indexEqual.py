# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:51:44 2018

@author: Tilak Upreti
"""

from math import * 

C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

D = input().split(',')    
D = [int(i) for i in D]   
D = [calc(i) for i in D]  
D = [round(i) for i in D] 
D = [str(i) for i in D]   

print(",".join(D))


