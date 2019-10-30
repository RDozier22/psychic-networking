#!/usr/bin/python3

for bottles in range (99,0,-1):
    if (bottles == 1):
        print("1 bottle of beer on the wall, 1 bottle of beer!")
        print("So take it down, pass it around, no more bottles beer on the wall")
    elif (bottles == 2):
        print("2 more bottles of beer on the wall, 2 more bottles of beer!")   
        print("So take it down, pass it around, 1 more bottles of beer on the wall")
    else:
        print(f"{bottles} of beer on the wall, {bottles} bottles of beer!")    
        print(f"So take it down, pass it around, {bottles-1} bottles of beer on the wall!\n")
