# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:12:56 2018

@author: Tilak Upreti
"""

t=1
for i in  range(t):
    a=input()
    ct=0
    ct1=0
    for j in range(len(a)):
        if a[j]=='1':
            ct=ct+1
        else:
            ct1=ct1+1
    
    if ct==1 or ct1==1:
        print('Yes')
    else:
        print('No')