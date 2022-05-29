#Udemy - Linked List Print List
#1/17/2022

#Regular Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
#Regular linked list class for the first part
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
################################################# New ############################################
#This is just surfing through the linked list
#We start at the head which is temp = self.head
#then as long as the temp next does not equal none, then we print it and move
#to the next node. This continues till we get to the end of the linked list 
#and the loop stops running.

#This is not built in but it is just added
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

#This is another extra created method      
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.print_list()


