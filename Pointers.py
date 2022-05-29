#Udemy - Pointers
#1/17/2022

#This is not a Pointer - This is where one variable refers to another and it is not 
#continuously updated as the original variable changes
num1 = 11

num2 = num1

print("Before value is updated:")
print("num1 =", num1)
print("num2 =", num2)

num1 = 22

print("\nAfter value is updated:")
print("num1 =", num1)
print("num2 =", num2)

#Using a Pointer
#dict1 is setting a pointer to value 11
#when you use dictionaries then when you say dict2 = dict1 it actually means dict2 = dict1 
#Rather than it referencing dict1's value

dict1 = {'value': 11}
dict2 = dict1

print("Before value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

dict1['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)