#!/usr/bin/python3
import random

choices=("Cannot predict now","Ask again later","Yes","No","Maybe", \
        "That is correct")

value=random.randint(0,len(choices)-1)

print(choices[value])
