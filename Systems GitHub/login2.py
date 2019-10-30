#!/usr/bin/python3

'''
Pseudo Code:
Establish Lists for Usernames and Passwords
Establish variables for prompting user for username and password
Establish nsted if statements, checking if username and passwords are correct
create a loop that only allows 5 logins
'''
uList = ['Ryan', 'root', 'admin', 'Admin']
pList = ['password', 'Admin', 'admin', 'root']

x=0

while (x < 5):
    Username = input('Username: ')
    Password = input('Password: ')
    if (Username) == (uList) and (Password) == (pList):
        print('Thinking.......')
        print('Your welcome, I am here for you to work......')
    else:
        print ("Input Error; re-enter a valid username or password")
        x = x + 1
