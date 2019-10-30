#!/usr/bin/python3

''' Pseudo Code
Establish variable for grade
Establish if statement for grade A
Establish elif statement for grade B-F
Print statements for each letter grade
Establish else statement if it is not a number'''

grade = input ("Enter a grade between 1 - 100: ")

if (int(grade) >= 90):
    print ("A")
elif (int(grade) >= 80):
    print ("B")
elif (int(grade) >= 70):
    print ("C")
elif (int(grade) >= 60):
    print ("D")
elif (int(grade) >= 1):
    print ("F")
else:
    print ("Input Error; re-enter a valid number")
