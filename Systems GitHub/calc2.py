#!/usr/bin/python3

'''
Pseudo Code:
Step 1: Build basic calculator script
Step 1a: Build predefined functions
Step 2a: Define main function
Step 2: Print statement that tells user that it is a calculator
Step 3: Establish variables as integers that ask user to provide x and y input
Step 4: Estabish variable that asks user to select Add, Sub, Mul, or Div
Step 5: Establish input validation for number length
Step 6: Establish if statement for first choice
Step 7: Establish print statements for if statement
Step 8: Establish elif statements for following three choices
Step 8a: Establish statement so you cannot divide by 0
Step 9: Establish print statements following three elif choices
Step 10: Establish else statement if user does not input correct functions
'''
def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y
 
def main():
    print ('Basic Calculator 2')
    choice=input("add, sub, mul, or div' ('add' or 'sub' or 'mul' or 'div')?") 
    x = input('Input number: ')
    y = input('Input number: ')

    if len(x) > 10:
        exit ('You must chose a number less than 10')
    elif len(y) > 10:
        exit ('You must chose a number less than 10')
    else:
        x = int(x)
        y = int(y)

    if choice == 'add':
        answer=addition(x,y)
        print ('You chose Addition')
        print (f'Your answer is: {answer}')
    elif choice == 'sub':
        answer=subtraction(x,y)
        print ('You chose Subtraction')
        print (f'Your answer is: {answer}')
    elif choice == 'mul':
        answer=multiplication(x,y)
        print ('You chose Multiplication')
        print (f'Your answer is: {answer}')
    elif (choice == 'div') and ('x == 0') or ('y == 0'):
        exit ('You cannot DIVIDE by 0')
    elif choice == 'div':
        answer=division(x,y)
        print ('You chose Division')
        print (f'Your answer is: {answer}')
    else:
        print ('You did not chose a correct calculator function')

main()
