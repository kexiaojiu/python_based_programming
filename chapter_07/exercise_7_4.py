#!/usr/bin/env pyhton3
pizza = "\nPlease enter dosing for the pizza."
pizza += "\nAnd enter 'quit' to quit.\n"

message = ""

while message != 'quit':
	message = input(pizza)
	if message != 'quit':
		print("We will add " + message + " in the pizza.")
	
