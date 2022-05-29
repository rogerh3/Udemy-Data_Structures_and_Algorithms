#Roger H Hayden III
#Binary Search Tree with Notes
#1/21/2022

#Construct the Node class with a left and right 
#Same set up as all other node classes just different labels
from turtle import left


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
#Binary Search Tree Class
#We set a root equal to none
class BinarySearchTree:
    def __init__(self):
        self.root = None

#Insert Method
#We go to create a new node, if self.root is none then change the root equal to the 
#new node.
#If this is not the case then set temp = root
#From here if the new node value is equal to another node value in the tree, 
#then return FALSE.
#If the new node is less than the temp value and if the left next is none, 
#then set the new node as temp.left and return TRUE.
#If the spot is not open then the temp value moves to the temp.left value.
#Else - if the temp.right is none, then add the new node to the right and return
#TRUE, but is this is not the case then move temp to temp.right.
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

#Contains Method - See if a tree contains a value
#Set temp to self root. If the root is none, return FALSE
#If not then check for if the value is less than the temp value, if it is
#set the temp = temp.left, elif the value is greater than the temp.value
#then set temp.right.
#This will keep going through until it reaches the end of the tree and it will
#return TRUE if you reach the value and if not then it will return FALSE.
    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

 #Method to return the minimum value
 #While the node.left is not none, set current node to the node.left.
 #Do this until there is no node to the left then return that value.   
    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node
        


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print(my_tree.contains(27))

print(my_tree.contains(17))

print(my_tree.root.value)
print(my_tree.root.left.value)                

print(my_tree.min_value_node(my_tree.root))
print(my_tree.min_value_node(my_tree.root.right))