#Roger H Hayden III
#Full Doubly Linked with Notes
#1/20/2022

#A Doubly Linked list is a list where there are pointers going in both directions

#Same as the Normal Node class for Linked Lists but we add self.prev = None as well
#since we will have to have pointers going both direction.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
#The Doubly Linked List Class is the same as the Linked List Class
#The only difference is the Node class above is different
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

#Normal / Same Print List Method
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

#New Doubly Linked List Append Method  
#Here we create the new node, and if self.head is none then the head and tail point to the new node.
#If that is false then set the tail.next = new node and set the new node prev = old tail      
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

#New Doubly Linked List Pop Method
#If length is equal to 0 then we return none
#If lenth is 1 then set head and tail to none then there are no nodes
#If there is more than 1 node then set tail to the node infront of the tail, then set the 
#tails prev next value to none to drop off the pointer to the last node then set temp.prev
#to none to break the pointer going back from the tail.
#Then we take one away from the length of the doubly linked list.
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

#New Doubly Linked List Prepend Method
#We create a new node and check the length of the doubly linked list
#if the length is 0 then set the head and tail both to the new node.
#If the doubly linked list has items, then set the new node.next = self.head
#or the current head. Then set the self head.prev = new node so it points back
#to the new node as well. Then we set the head to the new node and incrase the 
#doubly linked lists length by 1.
#Then we optionally return TRUE.
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

#Normal / Same Set Value Method as Linked Lists        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

#New Doubly Linked List Insert method
#Check the index passed, if it is not in the linked list then return FALSE
#If the index is 0 then prepend the Node
#If the index is equal to the length then append the Node
#If you add it somewhere in the middle we create a before and after variable
#the before will be the index - 1 and after will be before.next
#then we will put the new node.prev = before and new node.next = after
#and set the before.next = new node and after.prev = new node.
#Then we will increase the length of the doubly linked list by 1 and return TRUE.    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True  

#New Doubly Linked List Remove Method
#Check the index and if it is not within the list the return none
#If the index is equal to 0 then pop the first node
#If the index is equal to the list length - 1 then pop the last node
#If it is in the middle somewhere then set a temp value and remove the 
#temp next and prev and take away 1 from the length then return temp.
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp