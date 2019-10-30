#!/usr/bin/python3

''' Pseudo Code
Establish variable for grade
Establish if statements for grades A-F
Print statements for each letter grade
Establish else statement if it is not a number'''

grade = input ("Enter a grade between 1 - 100: ")

if (int(grade) >= 90):
    print ("A")
else:
    if (int(grade) >= 80):
        print ("B")
    else:
        if (int(grade) >= 70):
            print ("C")
        else:
            if (int(grade) >= 60):
                print ("D")
            else:
                if (int(grade) == 1):
                    print ("F")
                else:
                    print ("Input Error; re-enter a valid number")
