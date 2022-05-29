#Udemy - Taking a look at Classes
#1/17/2022

#Creating the Coookie class
#__init__ is the constructior
#this is a method that is a part of the class since it says self

#get_color is a method to recieve the color and return it

#set_color sets the color of the cookie
class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())
