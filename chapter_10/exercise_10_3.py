#!/usr/bin/env python3

filename = 'guest.txt'

with open(filename, 'w') as fo:
	message = "Please input your name: \n"
	fo.write(input(message) + "\n")
