#!/usr/bin/env python3
age = "\nPlease enter your age(enter 'q' to quit):"

active = True

while active:
	message = input(age)
	if message.lower() == 'q':
		print("Bye! Thank you for using this program!")
		break
	
	if int(message) < 3:
		price = 0
	elif int(message) < 12:
		price = 10
	elif int(message) > 12:
		price = 15
	else:
		print("Please try a again!\n")
		continue

	print("Your age is " + message + ". And the ticket price is $ " + str(price) + ".")	
		
