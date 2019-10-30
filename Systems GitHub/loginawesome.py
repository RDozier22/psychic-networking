import sys, getpass, hashlib

def main():
   
   uname = input('Username: ')
   passwd = getpass.getpass()
   salt = '#*&!678GHDF'
   password = (passwd + salt)
   p = hashlib.sha256(password.encode())
   userName = ('test','admin','root')
   count = 1
   passw=open('hashtable.txt', 'r')
   list.append(passw:readline())
   
   while uname == userName and p == passw:
       
       if count == 5:
           sys.exit('All attempts used. Quitting...')
       
       if len(passw) < 10 and len(passw) > 15:
           #print("Invalid input")
           val = False
      
      # if len(passw) > 15:
       #    print("Invalid input")
        #   val = False
       
       elif userDict.get(uname) == passw:
           print('Logging in...')
           break
       
       else:
           print('Invalid username or password. Try Again.')
           uname = input('Username: ')
           passw = getpass.getpass()
           count += 1
try:
   main()

except KeyboardInterrupt:
   print("\nExiting Program")

except ValueError:
   print("\nExiting Program")

except NameError:
   print("\nExiting Program")

except SystemExit:
   print("\nExiting Program")

except:
   print("Exiting Program")