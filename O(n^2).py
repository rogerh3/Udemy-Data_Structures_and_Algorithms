#Udemy - O(n^2)
#1/14/22

#Here we take the loops we used for O(n) - Drop constant, but put the loop for j inside of the i loop
#Program for O(n)- Drop Constant
#def print_items(n):
#    for i in range(n):
#        print(i)
    
#    for j in range(n):
#        print(j)

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j) 

print_items(10)
