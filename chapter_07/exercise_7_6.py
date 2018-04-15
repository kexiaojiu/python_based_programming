#!/usr/bin/env pyhton3
pizza = "\nPlease enter dosing for the pizza."
pizza += "\nAnd enter 'quit' to quit.\n"

active = True

while active:
	message = input(pizza)
	if message != 'quit':
		active = True
		print("We will add " + message + " in the pizza.")
	else:
		active = False

