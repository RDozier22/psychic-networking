#!/usr/bin/python3

'''
Pseudo Code:
Step 1: Build basic calculator script
Step 2: Print statement that tells user that it is a calculator
Step 3: Establish variables as integers that ask user to provide x and y input
Step 4: Estabish variable that asks user to select Add, Sub, Mul, or Div
Step 5: Establish input validation for number length
Step 6: Establish if statement for first choice
Step 7: Establish print statements for if statement
Step 8: Establish elif statements for following three choices
Step 8a: Establish statement so you cannot diivde by 0
Step 9: Establish print statements following three elif choices
Step 10: Establish else statement if user does not input correct functions
'''

print ('Calculator')

x = input('Input 1st number: ')
y = input('Input 2nd number: ')

choice = input("add, sub, mul, or div' ('add' or 'sub' or 'mul' or 'div')?")
if len(x) > 10:
    exit ('You must chose a number less than 20')
elif len(y) > 10:
    exit ('You must chose a number less than 20')
else:
    x = int(x)
    y = int(y)

if choice == 'add':
    print ('You chose Addition')
    print ('Your answer is: ',x + y)
elif choice == 'sub':
    print ('You chose Subtraction')
    print ('Your answer is: ',x - y)
elif choice == 'mul':
    print ('You chose Multiplication')
    print ('Your answer is: ',x * y)
elif (choice == 'div') and ('div == 0'):
    print('You cannot DIVIDE by 0')
    pass
elif choice == 'div':
    print ('You chose Division')
    print ('Your answer is: ',x / y)
else:
    print ('You did not chose a correct calculator function')
