#Udemy - Linked List Pop
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

#Normal Print List Method
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

#Normal Append Method        
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

#Here is the pop method
#To begin, we have that if the length of the linked list is 0 then return none
#If this is false then we set temp and pre both to the head node.
#Then we say while temp.next exists or is not none, then pre will move up to equal
#temp and then temp will move to next again. 
#This will keep happening until there is no next after temp, or in other words the 
#next is none and there is no further that it can go.
#Once we reach the end, then we set the tail to pre, set next to none, and subtract 1 length.
#Then at the end we check if length = 0, if it does then head and tail are both none.
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
        return temp.value


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop())
# (1) Item -  Returns 1 Node
print(my_linked_list.pop())
# (0) Items - Returns None
print(my_linked_list.pop())


