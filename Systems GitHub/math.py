#!/usr/bin/python3
import math

'''
Pseudo Code:
Step 1: Import math functions
Step 2: def area of circle
Step 3: define circumference
Step 4: Build if statement, with special statement for later call if needed
'''

def area_of_circle(rad):
    return round(math.pi * rad**2,2)

def circumference_of_circle(rad):
    return round(math.pi * 2 * rad,2)

if__name__=='__main__':
    radius = int(input("What is the radius? "))
    print("The area is ", area_of_circle(radius))
    print("The circumference is ",circumference_of_circle(radius))


