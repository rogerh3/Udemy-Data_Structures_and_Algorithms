#Udemy - Doubly Linked List Pop First
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

#Normal Doubly Linked List Prepend Method
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

#New Doubly Linked List Pop First Node Method
#We mus check the length of the doubly linked list.
#If it is 0, then return none as there are no Nodes.
#After this before we move foward we must set a temp value equal to the head.
#If it is 1 then set the head and tail to none then we have no Nodes again.
#If it is greater than 1, then we set the self head to the node after the head
#or self.head.next.
#Then we must change the self head.prev to none to remove the pointer going back to the
#first node, as well as changing the temp.next pointer to none so there is no pointer
#pointing back to the rest of the list.
#Then we remove 1 from the length and return temp.
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None      
        self.length -= 1
        return temp


my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(1)


# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop_first())
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop_first())
# (0) Items - Returns None
print(my_doubly_linked_list.pop_first())

