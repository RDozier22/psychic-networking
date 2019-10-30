#!/usr/bin/python3

def perimeter(length,width):
    return 2*length + 2*width

def area_of_circle(radius):
    return 3.14 * radius**2

def main():
    print ("Main Function")
    x = int(input("Length: "))
    y = int(input("Width: "))
    print(perimeter(x,y))
    z = int(input("Radius: "))
    print(area_of_circle(z))

main()
