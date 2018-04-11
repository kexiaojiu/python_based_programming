#!/usr/bin/env python3 
number = input("Enter a number, and I'll tell you if it's multiple of ten:")
number = int(number)

if number % 10 == 0:
	print("\nThe number " + str(number) + " is multiple of ten.")
else:
	print("\nThe number " + str(number) + " isn't' multiple of ten.")
