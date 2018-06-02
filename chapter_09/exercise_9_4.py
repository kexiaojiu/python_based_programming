#!/usr/bin/env python3

class Restaurant():
	"""a class for restaurants"""
	
	def __init__(self, restaurant_name, cyusune_type):
		self.restaurant_name = restaurant_name
		self.cyusune_type = cyusune_type
		self.number_served = 0
	
	def describe_restaurant(self):
		print("restaurant_name:" + self.restaurant_name)
		print("cyusune_type:" + self.cyusune_type)

	def open_restaurant(self):
		print("The " + self.restaurant_name.title() + " is open now.")
		
	def set_number_served(self, number):
		self.number_served = number
		
	def increment_number_served(self, add_number):
		self.number_served += add_number
		
	def print_number_served(self):
		print("There are " + str(self.number_served) + " men in the restaurant")
	
	

a_restaurant = Restaurant('jinguikezhan', 'chinese')
a_restaurant.describe_restaurant()
a_restaurant.open_restaurant()
a_restaurant.print_number_served()

a_restaurant.set_number_served(10)
a_restaurant.print_number_served()


a_restaurant.increment_number_served(10)
a_restaurant.print_number_served()
