#Udemy - Bubble Sort
#Roger H Hayden III
#1/31/2022

#We pass a list that we decide through the bubble sort
#We will take the lenth of the list - 1 then start at 0 and decrement
#each time. 
#In the second for loop we move forward through the list.
#Within this we will compare the number we are looking at to the number
#after it, if the number you are looking at, j, is larger then the number
#after, or j + 1, then move j infront and set j to j + 1 and keep going till
#you reach the end of the list or you reach a number that is larger then the one
#you are looking at. 
#If the next number is greater than the number you are on then we will leave it.
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0 ,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


print(bubble_sort([4,2,6,5,1,3]))

 