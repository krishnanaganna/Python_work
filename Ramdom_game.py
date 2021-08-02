# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

name = input("your name: ") 
print ('hello', name, 'lets play a game toghether')
low = int (input ("choose a lowest random number: "))
high = int (input("choose a highest random number: "))
x = random.randint(low, high)
for i in range(6):
    pred = int (input("Now Computer has a number its mind, guess it, you have 6 chances: "))
    if pred != x and i >= 5:
        print ("LOST GAME!!!")
    elif pred == x and i <= 2:
        print ("Good you predicted the number on attempt:",i)
        break
    elif pred == x and i <= 5: 
        print("You predicted the number too slow on attempt:",i)
        break
    else:
        print ("try again")
        
    