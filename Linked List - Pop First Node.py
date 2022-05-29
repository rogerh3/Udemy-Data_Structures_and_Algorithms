#Udemy - Linked List Popping off First Node
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

#Normal Prepend Method
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

#New Pop First Node Method
#We begin by saying if the length of the linked list is 0 then we return none since 
#there is no Nodes.
#If it is larger than 0 then we set temp equal to the head of the linked list. Once
#we do that then we set the head equal to the next node.
#We then set the temp.next to none so that the first node is no longer connected
#and then take one away from the length since we removed the first node.
#Then we check and see if the length is 0, if it is then we set the tail to none.
#Then we return the temp which is the whole node, not the value
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp


my_linked_list = LinkedList(2)
my_linked_list.append(1)


# (2) Items - Returns 2 Node
print(my_linked_list.pop_first())
# (1) Item -  Returns 1 Node
print(my_linked_list.pop_first())
# (0) Items - Returns None
print(my_linked_list.pop_first())


