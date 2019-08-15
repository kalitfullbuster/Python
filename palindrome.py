# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:32:46 2018

@author: Tilak Upreti
"""



def isPalindrome(t): 
      

    rev = ''.join(reversed(t)) 
  
 
    if (t == rev): 
        return True
    return False
  
# main function 
t = input()
ans = isPalindrome(t) 
  
if (ans): 
    print("YES") 
else: 
    print("NO") 