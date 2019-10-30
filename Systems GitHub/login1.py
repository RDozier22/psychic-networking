#!/usr/bin/python3

'''
Pseudo Code:
Establish Lists for Usernames and Passwords
Establish variables for username and password
Establish if statement for 1st username and password
Establish elif statements for other usernames and passwords
Establish else statement if none of the entered characters are in the lists
'''

uList = ['Ryan', 'Ryan-2', 'User1', 'User2']
pList = ['C0rBr@y524831', 'Juniper1', 'Edgar2']

UN = input('Username: ')
PW = input('Password: ')

if UN == uList[0] and PW == pList[0]:
    print('Thinking.......')
    print('Ryan, your welcome for being here for you!') 
elif UN == uList[1] and PW == pList[1]:
    print ('Thinking.......')
    print ('Ryan-2, your welcome for being here for you!')
elif UN == uList[2] and PW == pList[2]:
    print ('Thinking.......')
    print ('User1, your welcome for being here for you!')
elif UN == uList[3] and PW == pList[3]:
    print ('Thinking.......')
    print ('User2, your welcome for being here for you!')

else:
    print ("Input Error; re-enter a valid username")
