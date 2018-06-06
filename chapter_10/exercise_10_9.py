#!/usr/bin/env python3

def print_animal_name(animal_filename):
	'''print names of animals in files'''
	try:
		with open(animal_filename) as fo:
			names = fo.read()
	except FileNotFoundError:
		#~ print("Sorry, the file" + animal_filename + " does no exits.")
		pass
	else:
		print("The names in " + filename + " are as following: \n" + names)
		
		
filenames = ['cat.txt', 'dog.txt', 'cats.txt']
for filename in filenames:
	print_animal_name(filename)
