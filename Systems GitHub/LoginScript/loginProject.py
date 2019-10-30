import sys
import getpass
import hashlib
import logging


logFile = open('log.txt')
logging.basicConfig(level=logging.DEBUG,
    filename='log.txt',
    filemode='a',
    format='%(asctime)s %(levelname)s %(message)s'
)


def main():
   
   uname = input('Username: ')
   passwd = getpass.getpass()
   
   salt = '#*&!678GHDF'  
   password = (passwd + salt)   
   p = str(hashlib.sha256(password.encode()).hexdigest().upper())
   hashTable = open('hashtable.txt')
   
   count = 1
   
   users = ['root',
        'Sean',
        'JT',
        'Ryan',
        'Chris'
    ]
   
   hashes = []
   
   line = hashTable.readline().rstrip()
  

   while line:
       hashes.append(line)
       line = hashTable.readline().rstrip()
   
   pairs = dict(zip(users,hashes))
       

   while count <= 5:
       
       if count == 5:
           logging.critical('Failed login. 5 attempts used')
           logFile.close()
           
           sys.exit("All attempts used. Quitting...")
           
       if len(passwd) < 8 and len(passwd) > 30:
           val = False
        
       elif pairs.get(uname) == p:
           print('Logging in...')
           
           logging.info('{} logged in'.format(uname))
           
           break
           
       else:
           print('Invalid username or password. Try Again.')
           
           logging.warning('Failed login attempt with username: {} and password: {}'.format(uname,passwd))
           
           uname = input('Username: ')
           passwd = getpass.getpass()
           
           salt = '#*&!678GHDF'
           password = (passwd + salt)
           p = str(hashlib.sha256(password.encode()).hexdigest().upper())
           
           count += 1


try:
   main()
   
except KeyboardInterrupt:
   logging.error('KeyboardInterrupt')
   logFile.close()
   
   print("\nExiting Program")
   
   sys.exit()
   
except ValueError:
   logging.error('ValueError')
   logFile.close()
   
   print("\nExiting Program")
  
   sys.exit()
   
except NameError:
   logging.error('NameError')
   logFile.close()
   
   print("\nExiting Program")
   
   sys.exit()
   
except TypeError:
   logging.error('TypeError')
   logFile.close()
   
   print("\nExiting Program")
  
   sys.exit()