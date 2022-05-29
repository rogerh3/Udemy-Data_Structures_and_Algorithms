#Udemy - Doubly Linked List Get
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

#Normal Doubly Linked List Pop First Node Method
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
#New Doubly Linked List Get Method
#We must check the index passed, if the index is does not lie in the list, return none.
#If it is less than half the length of the list, then we iterate through from the front
#with a temp value till we find the index we wanted.
#If it is greater than half the list, then we start at the tail and iterate back until we 
#reach the index we were looking for.
#Then we return temp.
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
        

my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)


print(my_doubly_linked_list.get(1))
print(my_doubly_linked_list.get(2))
