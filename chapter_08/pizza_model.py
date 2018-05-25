#!/usr/bin/env python3

def make_pizza(size, *toppings):
	"""print all toppings which customers had ordered"""
	print("\nMaking a " +str(size) +
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
	
