#Udemy - Dropping Non-Dominates
#1/14/22

#Here we take the loop we used for O(n^2) and instead of adding another nested loop like for
#O(n^3) we added another loop below
#In this case, the i and j loops have O(n^2) and the k loop has O(n)
#We would theoretically get O(n^2 + n) but the n in this case is non dominate and has no affect as n 
#gets larger, so we would call this O(n^2)

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    for k in range(n):
        print(k)

print_items(10)
