#!/usr/bin/python3
import random

userguess = int(input("Pick a umber between 1 and 10: "))

myguess = random.randint(1,10)

print ("Is your number" + str(myguess)+ "?")

if(myguess == userguess):
    print ("I guessed your number")
else:
    print("Oh, I guessed incorrectly!")
