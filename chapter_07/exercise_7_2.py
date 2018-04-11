#!/usr/bin/env python3

number = input("How many people will have diner here?")

number = int(number)

if number > 8:
	print("Sorry, there is no available table.")
else:
	print("Luckly, there are some available tables.")
