#!/usr/bin/env python3

class User():
	"""a class of users"""
	
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		
	def describe_user(self):
		print("Profile of the user:")
		print("	-name:" + self.first_name.title() + " " + self.last_name.title())
		print("	-age" + str(self.age))
		
	def greet_user(self):
		print("Hello, " + self.first_name.title() + " " + self.last_name.title())


user1 = User('ke','yiyi', 0.3)
user1.describe_user()
user1.greet_user()
