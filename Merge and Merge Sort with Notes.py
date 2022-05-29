#Udemy - Merge and Merge Sort
#Roger H Hayden III
#2/2/2022

#Merge Function
#Takes 2 sorted lists and puts them together.
#We start with 2 sorted lists
#Ex: 1,3,7,8 and 2,4,5,6
#Use while loops because we dont know how many times we will have
#to do this.
#We set i equal to the index 0 for the first list and
#j to the index 0 on the second list.
#Then we have our while loop that as long as we still have items in both
#lists then we keep going. If either list becomes empty we stop.
#If i < j then we append from list 1 the item at that index and then
#increment i by 1.
#If j < i then we append from list 2 the item at that index and then
#increment j by 1.
#If one of the lists ends before the other, then we go down to the bottom 
#while loops.
def merge(array1, array2):
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1

 #If one of the lists is longer than the other, then one of these while
 #loops below will run through the rest of the list that is left             
    while i < len(array1):
        combined.append(array1[i])
        i += 1

    while j < len(array2):
        combined.append(array2[j])
        j += 1

    return combined


#Takes a list that keeps breaking it in half until there
#are only lists of size 1, then you use merge to put them together.
#This is done using recursion.
#We say if our list length is 1, then return the list.
#If not then we divide our list in 2 (using int to make sure there is no decimals)
#and assign a left and right.
#Then we will do a merge, but do a merge sort within to make sure each list only
#has one item.
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))

print(merge([1,2,7,8], [3,4,5,6]))

print(merge_sort([3,1,4,2]))

