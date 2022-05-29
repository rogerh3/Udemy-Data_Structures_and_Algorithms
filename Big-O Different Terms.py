#Udemy - O(a+b) and O(a*b)
#1/17/22

#Here we take two seperate loops which would be O(n) through dropping the constant,
#but since there is 2 differrent terms passed through the loops we get O(a+b) and that 
#is as far as this can be simplified
def print_items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

print_items(1, 10)

#Here we do the same sort of thing as above but we have the second loop nested rather than
#external
def print_items(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)

print_items(1, 10)