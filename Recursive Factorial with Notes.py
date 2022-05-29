#Udemy - Recursive Factorial
#Roger H Hayden III
#1/31/2022

#We check if n is equal to 1, if so then retun 1
#If not then we retun n * factorial(n-1)
#This is the recursive part of the function where it 
#refers to itself.
#Once we reach 1 then the recursive function ends
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(4))

