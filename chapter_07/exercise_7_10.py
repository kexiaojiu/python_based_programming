#!/usr/bin/env python3

responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	place = input("\nIf you could visit one place in the world, where would you go?")
	
	responses[name] = place
	
	repeat = input("Another one?(yes or no)")
	if repeat == 'no':
		print("Thank you!")
		polling_active = False
	
print("\n------ Result------")
for name, place in responses.items():
	print(name.title() + " would go " + place.title())
