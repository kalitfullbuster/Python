# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 19:48:32 2018

@author: Tilak Upreti
"""

def check(S, N, M): 
  

    if (((N * 6) < (M * 7) and S > 6) or M > N):  
        print("NO") 
    else: 
          
   
        days = (M * S) // N 
          
        if (((M * S) % N) != 0): 
            days += 1
       
        print(days) 
 
num = input()
a = list(map(int, num.split()))
S=a[0]
N=a[1]
M=a[2]
check(S, N, M) 