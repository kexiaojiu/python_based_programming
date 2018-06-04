#!/usr/bin/env python3

filename = 'pi_digits.txt'

with open(filename) as  fn:
	lines = fn.readlines()

pi_string = ''

for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))
