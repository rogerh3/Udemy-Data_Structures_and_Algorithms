#Roger H Hayden III
#Queues with Notes
#1/20/2022

#Normal Node Class like Singly Linked List and Stacks
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
#Queue Class
#Like Singly Linked List but first and last rather than head and tail
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

#Print Method
#Same as Singly Linked Lists but use first rather than head
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

#Enqueue Method - Adding to queue
#If there is no Nodes, then create one and set first and last equal to it
#If there is Nodes, set self.last.next = new node, and the last = new node
#Then add to the length and return TRUE.
#The end of the Queue is on the right and not the left      
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

#Dequeue Method - Removing from Queue
#Check Length, if it is 0 then return none.
#If not, set temp = first node
#If the length is 1 then set first and last to none.
#If the length is longer than 1, then set the self.first = node after first
#Then change temp.next to none and the first Node will drop off.
#Then subtract 1 from the length and return the temp value.
#This removes the first node, or the one in the back of the line.
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

 
my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue())
# (1) Item -  Returns 1 Node
print(my_queue.dequeue())
# (0) Items - Returns None
print(my_queue.dequeue())