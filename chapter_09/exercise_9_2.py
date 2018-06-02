#!/usr/bin/env python3

class Restaurant():
	"""a class for restaurants"""
	
	def __init__(self, restaurant_name, cyusune_type):
		self.restaurant_name = restaurant_name
		self.cyusune_type = cyusune_type
		
	
	def describe_restaurant(self):
		print("restaurant_name:" + self.restaurant_name)
		print("cyusune_type:" + self.cyusune_type)
		
		
	def open_restaurant(self):
		print("The " + self.restaurant_name.title() + " is open now.\n")


a_restaurant = Restaurant('jinguikezhan', 'chinese')
a_restaurant.describe_restaurant()
a_restaurant.open_restaurant()


t_restaurant = Restaurant('jinguikezhan', 'chinese')
t_restaurant.describe_restaurant()
t_restaurant.open_restaurant()

f_restaurant = Restaurant('jinguikezhan', 'chinese')
f_restaurant.describe_restaurant()
f_restaurant.open_restaurant()
