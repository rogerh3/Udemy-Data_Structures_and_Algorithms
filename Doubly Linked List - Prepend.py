#Udemy - Doubly Linked List Prepend
#1/18/2022

#Normal Doubly Linked List Node Class
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

#Normal Doubly Linked List Append Method        
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

#Normal Doubly Linked List Pop Method
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

#New Doubly Linked List Prepend Method
#We create a new node and check the length of the doubly linked list
#if the length is 0 then set the head and tail both to the new node.
#If the doubly linked list has items, then set the new node.next = self.head
#or the current head. Then set the self head.prev = new node so it points back
#to the new node as well. Then we set the head to the new node and incrase the 
#doubly linked lists length by 1.
#Then we optionally return TRUE.
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True


my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(3)

my_doubly_linked_list.prepend(1)

my_doubly_linked_list.print_list()

