#!/usr/bin/env python3

import json

filename = 'number.json'

with open(filename) as f_obj:
	numbers = json.load(f_obj)
	
print(numbers) 
