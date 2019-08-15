# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:29:15 2018

@author: Tilak Upreti
"""
def getMissingNo(A): 
    n = len(A) 
    total = (n+1)*(n+2)//2
    sum_of_A = sum(A) 
    return total - sum_of_A 
  

A = [int(x) for x in input().split()]
miss = getMissingNo(A) 
print(miss) 