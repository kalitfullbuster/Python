# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 19:11:52 2018

@author: Tilak Upreti
"""
no = input()
print(no)
n = list(map(int, no.split()))
print(n)
for i in n:
    if(i==0):
        
        n.remove(i)
        n.append(0)
        n
        
s = ' '.join(str(e) for e in n)        
print(s)
