#Roger H Hayden III
#Stacks with Notes
#1/20/2022

#Same as a Linked List Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
#Stack Class
#Instead of head and tail we have top and bottom
#but we only keep track of the top and set the height
#as 1. 
#Visually the arrows would be pointing down here and not
#sideways like linked lists.
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

#Print Method
#This is the same print method from doubly and singly linked lists
#but we have self.top rather than self.head
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

#Push Method
#Push is when you push a new note onto the top of the stack
#Here we say if the hight is equal to 0 then we just add a new node.
#if not then we set the new node next equal to the top and then label 
#the new node as the top.
#Then we increase the height and return TRUE.
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

#Pop Method
#Check height, if it is 0 then return none.
#If it is not then set the temp value as the top.
#Set the top equal to the node after the top node.
#Then change the temp.next to none and remove 1 from the height.
#Return the temp value.
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    

my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

print(my_stack.pop(), '\n')

my_stack.print_stack()
