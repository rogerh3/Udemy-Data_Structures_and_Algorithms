#Roger H Hayden III
#Full Node Class, Linked List Class and Methods with Notes
#1/19/2022

from pickle import TRUE

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

#This is just surfing through the linked list
#We start at the head which is temp = self.head
#then as long as the temp next does not equal none, then we print it and move
#to the next node. This continues till we get to the end of the linked list 
#and the loop stops running.
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

#This is where the append method is created
#Here we set new_node=Node(value), but if there is no node, then we set
#the head and the tail to the new node.
#Then we go on and say if there is a node, then when we add a new one the tail
#needs to move to the new node. We are saying that the node after the tail is the new
#node and we say that tail should now be the new node.
#after this we increase the length of the linked list by 1.   
#At the end we optionally added that the code will say True if the tail is moved    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return TRUE

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

#Here is the Prepend Method
#First we look at the length of the node, if it is 0 then we add a new node
#and set the tail and head equal to the node.
#If the length is longer than 0 then we set the new node as the head and add
#one to the length of the linked list.
#We are optionally returning TRUE
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

#New Get Method
#Check if the index you are looking for is < 0 or >= the actual length of the linked list
#If these are both true then return none since there is no node there.
#We set temp equal to the head, then we essentually count each node until we get to the index
#we asked for. The for look will run the number of times that we pass through.
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

#New Set Value Method
#This will iterate through to a specific index then change its value        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

#New Insert Method
#Checking if the index and making sure it is in the linked list, if not return FALSE
#If the index is equal to 0 then just prepend the value
#If the index equals the length of the linked list then append the value to the end
#If none of these are true then find the index provided - 1, set a temp value, create a new
#value after temp, or temp.next, then add to the length of the linked list.
#Then we return an optional TRUE   
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  
  
#New Remove Method
#If the index does not exist in the linked list, return none
#If the index is 0 then pop the first node
#If the index is one less than the length of the linked list then pop the last node
#If none of those are true then go one index behind the one you want to remove, then set 
#a prev node there and set a temp node as prev.next. make prev.next=temp.next
#Then change temp.next to none so that the prev node no longer connects to the
#temp node and the temp node no longer connects to the next. Then the temp node is removed
#Then return the temp node.
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

#New Reverse Method
#We set temp = jead, then set the head=tail, then set tail = temp
#Once we do this then we set after = temp.next, and before infront of temp which is none at first
#Then this will iterate through the linked list and switch all the direction of the pointers
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after