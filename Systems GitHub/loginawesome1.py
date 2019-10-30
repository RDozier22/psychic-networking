import sys
import getpass
import hashlib
import logging
​
logFile = open('log.log.txt','a')
​
def main():
   uname = input('Username: ')
   passwd = getpass.getpass()
   salt = '#*&!678GHDF'
   password = (passwd + salt)
   p = hashlib.sha256(password.encode())
   userName = ('test','admin','root')
   count = 1
   passw=open('hashtable.txt', 'r')
   list.append(passw.readline())
   
   
   while uname == userName and p == passw:
       if count == 5:
           logFile.write(logging.critical('Failed login. 5 attempts used'))
           logFile.close()
           sys.exit('All attempts used. Quitting...')
           
       if len(passw) < 10 and len(passw) > 15:
           #print("Invalid input")
           val = False
      # if len(passw) > 15:
       #    print("Invalid input")
        #   val = False
        
       elif userDict.get(uname) == passw:
           print('Logging in...')
           logFile.write(logging.info('{} logged in'.format(uname)))
           logFile.close()
           break
           
       else:
           print('Invalid username or password. Try Again.')
           logFile.write(logging.warning('Failed login attempt with username: () and password: {}'.format(uname,passw)))
           uname = input('Username: ')
           passw = getpass.getpass()
           count += 1
           
try:
   main()
except KeyboardInterrupt:
   logFile.write(logging.error('KeyboardInterrupt'))
   logFile.close()
   print("\nExiting Program")
   sys.exit()
   
except ValueError:
   logFile.write(logging.error('ValueError'))
   logFile.close()
   print("\nExiting Program")
   sys.exit()
   
except NameError:
   logFile.write(logging.error('NameError'))
   logFile.close()
   print("\nExiting Program")
   sys.exit()
   
except SystemExit:
   logFile.write(logging.error('SystemExit'))
   logFile.close()
   print("\nExiting Program")
   sys.exit()
