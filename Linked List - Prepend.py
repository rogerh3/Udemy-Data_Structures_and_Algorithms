#Udemy - Linked List Prepend
#1/17/2022

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

#Normal Print Method
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

#Normal Append method        
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

#Normal Pop Method
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

#Here is the Prepend Method
#First we look at the length of the node, if it is 0 then we add a new node
#and set the tail and head equal to the node.
#If the length is longer than 0 then we set the new node as the head and add
#one to the length of the linked list.
#We are optionally returning TRUE
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


my_linked_list = LinkedList(2)
my_linked_list.append(3)

my_linked_list.prepend(1)

my_linked_list.print_list()

