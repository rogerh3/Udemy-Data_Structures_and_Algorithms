#Roger H Hayden III
#Hash Table - Items in Common Between 2 Lists
#1/23/2022

#This is O(n^2) - less efficient
#It iterates one index at a time from list1 and goes through all options
#in list2.
#If it reaches an item in common then it will return TRUE
#If not then it will return FALSE
def item_in_common1(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

#O(n) - Using Dictionaries - More Efficient
#Create a Dictionary from list1 O(n)
#Check if anything in list2 is also contained within the created dictionary
#If so then it will return TRUE, if not then FALSE.
def item_in_common2(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True

    return False


list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common1(list1, list2))

print(item_in_common2(list1, list2))