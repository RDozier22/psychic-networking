#!/usr/bin/python3

'''
Pseudo Code:
Step 1: Establish dictionary for Usernames and Passwords
Step 2: Establish variables for prompting user for username and password
Step 3: Establish nested if statements, checking if username and passwords are correct
Step 4: Create a loop that only allows 5 logins
'''
password = {'Ryan':'password', 'root':'root', 'admin':'admin', 'Admin':'Admin'}

x=0

while (x < 5):
    Username = input('Username: ')
    Password = input('Password: ')
    if Username in password:
        if password[Username] == Password:
            print('Your welcome, I am here for you to work......')
            break

    else:
        print ("Input Error; re-enter a valid username or password")
    x=x+1
