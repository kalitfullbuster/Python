# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 18:58:36 2018

@author: Tilak Upreti
"""

def  check(x):
    rem=0
    n=x
    while(n>0):
      
        t=n%10
        rem=rem+t
        n=n//10
    return rem





n=int(input())
result=check(n)
if(result>=10):
   result=check(result)

print(result)
