#!/usr/bin/python3
import math

radius = int(input("What is the radius? "))
value = round(math.pi*radius**2,10)

print("The area of a circle with a radius of", radius, "is", value)
print("The circumference of the circle is",round(2*math.pi*radius,10))
