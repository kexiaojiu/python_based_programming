#!/usr/bin/env python3

def make_sandwich(*toppings):
	print("\nMakinng a sandwich with the following toppings:")
	for topping in toppings:
		print("- " + topping)
		
make_sandwich('meat')
make_sandwich('rice', 'meat')
