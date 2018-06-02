#!/usr/bin/env python3

class Dog():
	"""a simple test for simulating dogs"""
	 
	def __init__(self, name, age):
		 """initialization"""
		 self.name = name
		 self.age = age
		 
	def sit(self):
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + ".")

my_dog.sit()
my_dog.roll_over()



your_dog = Dog('kk', 6)

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog's age is " + str(your_dog.age) + ".")

your_dog.sit()
your_dog.roll_over()
