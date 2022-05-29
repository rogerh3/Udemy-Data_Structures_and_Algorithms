#Udemy - Linked List Append
#1/17/2022

from pickle import TRUE

#Normal Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

#Normal Linked List Class
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

#Normal Print Class
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

#This is where the append method is created
#Here we set new_node=Node(value), but if there is no node, then we set
#the head and the tail to the new node.
#Then we go on and say if there is a node, then when we add a new one the tail
#needs to move to the new node. We are saying that the node after the tail is the new
#node and we say that tail should now be the new node.
#after this we increase the length of the linked list by 1.   
#At the end we optionally added that the code will say True if the tail is moved    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return TRUE



my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.print_list()


                                  