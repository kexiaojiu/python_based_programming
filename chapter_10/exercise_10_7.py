#!/usr/bin/env python3

def input_number():
	'''input a number'''
	num = input("\nInput a number: ")
	try:
		num = int(num)
	except ValueError:
		print("Sorry, you should input a number.")
	else:
		return num
	
print("Give me  two numbers, and I'll add them.")	
while True:
	flag_quit = input("Quit this program?(y/n,y to quit)\n")
	if flag_quit == 'y' or flag_quit == 'Y':
		print("Thanks!")
		break
		
	first_number = input_number()
	second_number = input_number()
	
	try:
		answer = first_number + second_number
	except TypeError:
		print("Please try another two numbers again.\n")
	else:
		print("The answer is " + str(answer) + "\n")
