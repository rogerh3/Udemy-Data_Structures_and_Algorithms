#Udemy - Selection Sort
#Roger H Hayden III
#2/2/2022

#We create an initial for loop that will loop through the length of the list - 1 for the index values
#Then we will set the min = i which will increase by 1 for each loop through.
#The for loop for j starts our beginning value as i + 1, and end as the length of the list or the last index
#i is essentually index 0 to start and j is i + 1 or index 1.
#This will compare i to j, if j is lower then set min = j, else keep i
#This will continue through until you reach the last index.
#The last for loop switches the value at the min index and the value of the index you began at
def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


print(selection_sort([4,2,6,5,1,3]))

