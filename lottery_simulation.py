# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 20:01:06 2018

@author: Tilak Upreti
"""

import random
import matplotlib.pyplot as plt


account = 0
x = []
y = []
for i in range(365):
    x.append(i+1)
    bet = random.randint(1,10)
    lucky_draw = random.randint(1,10)
    
    if bet == lucky_draw:
        account = account + 900-100
    else:
        account=account-100
    
    y.append(account)
print("Amount in your account is:" ,account)
plt.plot(x,y)
plt.show()