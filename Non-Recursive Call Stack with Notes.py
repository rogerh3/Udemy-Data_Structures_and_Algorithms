#Udemy - Call Stack
#Roger H Hayden III
#1/31/2022

#This is a call stack that does not have any recursion
#All of these functions are none recursive

#Function Three prints itself
def funcThree():
    print('Three')

#Function two calls function 3 and prints two
def funcTwo():
    funcThree()
    print('Two')

#Function one calls function 2 and prints one
def funcOne():
    funcTwo()
    print('One')

#This ends up printing three, two, one since each of these all reference
#within themselves.
funcOne()

