#Udemy - O(n) Drop Constant
#1/14/22

#This outputs 0-9 twice
#Therefore it runs n+n times
#Instead of this being O(2n) it is O(n) since you drop the constant
def print_items(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

print_items(10)
