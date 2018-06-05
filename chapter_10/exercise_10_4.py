#!/usr/bin/env python3

filename = 'guest_book.txt'

flag = input("Welcome to this program. Enter 'q' to quit: ")

while (flag != 'q'):
	with open(filename, 'a') as fo:
		name = input("Please input your name: \n")
		print("Hello, " + name.title())
		fo.write(name.title() + "\n")
	flag = input("\nEnter 'q' to quit:\n")
