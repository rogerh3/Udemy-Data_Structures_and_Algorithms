#Udemy - O(n^2)
#1/14/22

#Here we take the loop we used for O(n^2) and add another nested loop
#Program for O(n^2)
#def print_items(n):
#    for i in range(n):
#        for j in range(n):
#            print(i,j) 

def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

print_items(10)
