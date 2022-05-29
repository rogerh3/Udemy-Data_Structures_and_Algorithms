#Udemy - Linked List Constructor
#1/17/2022

#Node class will only contain a constructor and a value
#Initially once used there will be one value and no next if there is only one node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
#The Constructor def __init__(self,value) - is going to crate a new node
#new_node crates a node
#self.head makes the node the head 
#self.tail makes the node also the tail
#self.length tracks the length of the list which is 1 currently
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

 
#Here we are calling the LinkedList class and assigning the value of 4 to that new node
#Link list would be a length of 1
my_linked_list = LinkedList(4)

print(my_linked_list.head.value)


                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
