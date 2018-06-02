#!/usr/bin/env python3

class User():
	"""a class of users"""
	
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.login_attempts = 0
		
	def describe_user(self):
		print("Profile of the user:")
		print("	-name:" + self.first_name.title() + " " + self.last_name.title())
		print("	-age" + str(self.age))
		
	def greet_user(self):
		print("Hello, " + self.first_name.title() + " " + self.last_name.title())

	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def restet_login_attempts(self):
		self.login_attempts = 0
		
	def print_login_attempts(self):
		print("Login attempts: " + str(self.login_attempts) + "\n")
		
		
class Admin(User):
	def __init__(self, first_name, last_name, age, privileges):
		super().__init__(first_name, last_name, age)
		self.privileges = privileges
		#"can add post, can delete post, can ban user"
		
	def show_privileges(self):
		print("Privileges: " + self.privileges)


admin = Admin('ke', 'yiyi', 3, "can add post")
admin.greet_user()
admin.show_privileges()
