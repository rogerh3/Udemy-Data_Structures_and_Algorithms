#Roger H Hayden III
#Hash Table with notes
#1/23/2022

#Hash Table Class
#We made the size of the hash table as 7 which is the defult address size
#We call this list data_map and set it equal to none * size
#So this list will have 7 addresses that all contain None
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

#Hash Method
#What the key, value pair is passed through
#Initialize this to 0 
#Then we will loop through the letters that are in the key that we passed
#through the hash method.   
#ord(letter) gets the ordinal of each letter, or the ascii number for each letter and 
#multiply it by 23 because 23 is a prime number, you can use any prime number here.
#Then we have a modulo operator % which gives you the remainder of this calulation 
#divided by the length of the hash table, or data_map.
#Then we return the number that is my_hash, in this case since the length of the data_map
#is 7, this would return a number between 0 and 6.
#IMPORTANT: my_hash will be the address where the key, value pair is placed
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

#Print Method
#For all addresses i, this will print in the following way
#address : value
#Example: 
#0 : None
    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

#Set Method
#We first need to figure out the address we want to assign the key, value pair to
#We set index = self.__hash(key) which will pass the key through the hash method
#This will set the key, value pair to an address
#If an empty set in an address within the hash table is not created yet, or if 
#data_map = None, then we create an empty set (list) in that address so that we can 
#fill that empty set (list).
#Now that there is an empty set (list) in that address spot, then we can append
#the key and value into the list at the correct address.
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

#Get Method
#Here we want to assign the index= __hash(key) again to attempt to find the 
#index or address of that key.
#We go to say if that index is not none, then we can loop through the items 
#in that index to find the one that we are looking for (the list in the address).
#This for loop keeps running until we get to the value we are looking through.
#Once we find the item we are looking for then we return it.
#If the key is not in the hash table, once you loop through it all, it will return none.   
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

#Keys Method
#This takes all of the keys from the hash table, puts them into a list and then returns the list.
#We have a for loop that goes through all of the addresses until we reach the end.
#If any given address is none then we skip it, if it is not none, then we have another for loop
#that goes through the list within each address.
#All of these values will be appended to the empty list all_keys, and once you get through this whole
#thing and return all_keys, the list will be all of the keys that exist in the hash table.
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
        

my_hash_table = HashTable()

my_hash_table.print_table()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))

print(my_hash_table.keys())



