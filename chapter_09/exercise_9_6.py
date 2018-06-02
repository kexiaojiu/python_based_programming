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
		
		
class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cyusune_type, flavors):
		super().__init__(restaurant_name, cyusune_type)
		self.flavors = flavors
	
	def describe_ice_cream(self):
		print("FLavors: " + str(self.flavors))
		
ice_cream_stand = IceCreamStand('kk', 'w', ['p1', 'p2'])
ice_cream_stand.describe_restaurant()
ice_cream_stand.describe_ice_cream()
