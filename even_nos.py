# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 11:14:53 2018

@author: Tilak Upreti
"""

y=input()
y=y.split(",")

a=int(y[0])
b=int(y[1])
values = []
for i in range(a, b+1):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print (",".join(values))