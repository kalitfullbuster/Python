# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:48:45 2018

@author: Tilak Upreti
"""



def namec(name):
    s=range(len(name))
    i=count=0
    for i in s:
        
      if name[i]=='A':
          count+=1
    
      if name[i]=='B':
          count+=2
          
      if name[i]=='Q':
          count+=1
          
      if name[i]=='R':
          count+=1
          
      if name[i]=='D':
          count+=1
       
        
      if name[i]=='O':
          count+=1
          
      if name[i]=='P':
          count+=1
   
    ans = count
    print(ans)
    
name =input()
namec(name)


