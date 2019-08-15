# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:41:46 2018

@author: Tilak Upreti
"""

import random

def choose():
             words = ['example','elephant','cat','computer','bird']
             pick = random.choice(words)
             return pick
     
def jumble(word):
         jum = "".join(random.sample(word,len(word)))
         return jum
     
        
def play():
         p1name = input('Player 1 Enter Your Name:')
         p2name = input("Player 2 Enter Your Name:")
         p1pts = 0
         p2pts = 0
         turn = 0
         while(1):
             picked_word =choose()
             ques = jumble(picked_word)
             print(ques)
             if turn%2 == 0:
                 print(p1name ,'Your turn')
                 ans = input("Give Your Answer")
                 if ans == picked_word:
                     p1pts = p1pts + 1
                     print('Your Score is:' ,p1pts)
                 else:
                    print("Better Luck Next Time. Ans was:" ,picked_word)
                    c = input('Press 1 to Continue 0 to Quit')
                    if c == 0:
                     break
             else:
                print(p2name ,'Your turn')
                ans = input("Give Your Answer")
                if ans == picked_word:
                     p2pts = p2pts + 1
                     print('Your Score is:' ,p2pts)
                else:
                    print("Better Luck Next Time. Ans was:" ,picked_word)
                    c = input('Press 1 to Continue 0 to Quit')
                    if c == 0:
                        break
                    
         turn=turn + 1
play()
    

