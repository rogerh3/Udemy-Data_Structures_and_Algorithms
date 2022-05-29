#Udemy - Doubly Linked List Append
#1/18/2022

#Normal Doubly Linked List Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
#Normal Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

#Normal Print Method
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

#New Doubly Linked List Append Method  
#Here we create the new node, and if self.head is none then the head and tail point to the new node.
#If that is false then set the tail.next = new node and set the new node prev = old tail      
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
  

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

my_doubly_linked_list.print_list()

