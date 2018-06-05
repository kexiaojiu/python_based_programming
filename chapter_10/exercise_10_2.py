#!/usr/bin/env python3

filename = 'learning_python.txt'

with open(filename) as fo:
	lines = fo.readlines()
	
for line in lines:
	print("Before: " + line)
	print("After:  " + line.replace('python', 'C'))
