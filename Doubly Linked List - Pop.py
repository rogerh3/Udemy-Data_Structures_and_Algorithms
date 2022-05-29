#Udemy - Doubly Linked List Pop
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

#Normal Print List Method
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

#New Doubly Linked List Pop Method
#If length is equal to 0 then we return none
#If lenth is 1 then set head and tail to none then there are no nodes
#If there is more than 1 node then set tail to the node infront of the tail, then set the 
#tails prev next value to none to drop off the pointer to the last node then set temp.prev
#to none to break the pointer going back from the tail.
#Then we take one away from the length of the doubly linked list.
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
  

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)


# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop())
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop())
# (0) Items - Returns None
print(my_doubly_linked_list.pop())

