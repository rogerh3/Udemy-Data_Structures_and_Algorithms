#Udemy - Depth First Search - Pre-Order, Post-Order, and InOrder Methods
#Roger H Hayden III
#2/5/2022

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

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


    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
#Depth First Search Pre-Order
#We create a results list
#From here we have a traverse function within this method
#Traverse will be passed a node and we will take the value and write it in
#the results list.
#From here we will traverse the left and right nodes if they are not equal to None.
#After this we call the function beginning with the root of the tree and this creates
#a call stack to traverse the tree in such a way going down the left then going to the right.
    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

#Depth First Search Post Order
#Create the result list
#We have the same traverse function as Pre-Order
#But this time we will got left, then right, then append the value at the end 
#rather than the beginning.
    def dfs_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

#Depth First Search In Order
#Create the Result list
#Bring in the Traverse function again
#Here we go left, write the value, then go right
#Once again this just works in a different order.
    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value) 
            if current_node.right is not None:
                traverse(current_node.right)          
        traverse(self.root)
        return results
        

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_pre_order())

print(my_tree.dfs_post_order())

print(my_tree.dfs_in_order())

# [18, 21, 27, 47, 52, 76, 82]
                



 