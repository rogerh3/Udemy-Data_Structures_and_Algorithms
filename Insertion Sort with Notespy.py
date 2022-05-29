#Udemy - Insertion Sort
#Roger H Hayden III
#2/2/2022

#An Insertion Sort compares a value to the one before it.
#Our range goes from index 1 to the last index
#Set temp value equal to the index of 1, make j the value before it.
#Compare the values and if the one in front is larger, switch them, if not
#then continue on.
#This process will continue until the list is sorted.
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j] 
            my_list[j] = temp
            j -= 1
    return my_list


print(insertion_sort([4,2,6,5,1,3]))

