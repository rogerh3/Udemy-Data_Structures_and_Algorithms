#Udemy - Pivot and Quick Sort
#Roger H Hayden III
#2/3/2022

#Swap Function
#This swap function is created so that we can use it in the pivot function.
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


#Pivot Function
#The pivot function moves everything less than the first index to the left and
#everything greater to the right after the initial quick sort is done
#To run this we must pass the list, pivot index, and end index
#If you have a 7 item list the pivot index is 0 and the end index is 6.
#We set the swap index equal to the pivot index.
#Then we set our for loop range to the pivot index + 1 and the end index + 1.
#The reason for this is so the for loop goes up to but not including the index after the list.
#If the value for each index (i) is less than the pivot index value, then move the swap index inbetween
#the pivot index and i and swap the index values of i and the swap values.
#Then at the end we must swap items from the pivot index with the items smaller then the value at index 0 on 
#the left and the larger on the right.
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


#Quick Sort Helper Function
#Looks to see if the left value is smaller than the right - Base Case
#If so then we set the pivot index.
#We will focus at the beginning of the list then continue to use the quick sort from
#the small values in the front then the larger values at the end.
#This is done from recursively calling quick sort.
def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)  
        quick_sort_helper(my_list, pivot_index+1, right)       
    return my_list

#Quick Sort Function
#Uses the quick sort helper to quick sort the list
#This will also find the first and last index
def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

my_list = [4,6,1,7,3,2,5]

print(pivot(my_list, 0, 6))

print(my_list)

print(quick_sort([4,6,1,7,3,2,5]))