#!/bin/python3

import mods
import sys
import getpass

#create input fields
uname = input('Username: ')
passw = getpass.getpass(prompt='Password: ')

#create dictionaries containing username and password
userDict = {'test':'password','admin':'admin','root':'root'}

#create attempt counter
count = 1


#create while loop for attempt couter
while True
    try:
        if uname==userDict

#create conditionals based on username and password and attempt count
    if count == 5:
        sys.exit('All attempts used. Quitting...')
        
    elif userDict.get(uname) == passw:
        print('Logging in...')
        break

    else:
        print('Invalid username or password. Try Again.')
        uname = input('Username: ')
        passw = getpass.getpass(prompt='Password: ')
        count += 1