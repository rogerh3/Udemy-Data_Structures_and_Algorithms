#Udemy - Doubly Linked List Constructor
#1/18/2022

#A Doubly Linked list is a list where there are pointers going in both directions

#Same as the Normal Node class for Linked Lists but we add self.prev = None as well
#since we will have to have pointers going both direction.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
#The Doubly Linked List Class is the same as the Linked List Class
#The only difference is the Node class above is different
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

#Normal / Same Print List Method
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
  

my_doubly_linked_list = DoublyLinkedList(7)

my_doubly_linked_list.print_list()




