# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:40:01 2018

@author: Tilak Upreti
"""

def fadedP(s):
    length = len(s)
    slist = []
    slist.extend(s)
    for i in range(length//2):   
        if slist[i] != '.' and slist[length-1-i] != '.' and slist[i] != slist[length-1-i]: 
            print(-1)
            return
    for i in range(length):      
        if slist[i] == '.' and slist[length-1-i] != '.': 
            slist[i] = slist[length-1-i]
        elif slist[i] == '.':                         
            slist[i] = 'a'
    print("".join(slist))
    
fadedP(input())