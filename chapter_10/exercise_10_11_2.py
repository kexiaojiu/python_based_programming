#!/usr/bin/env python3
import json

filename = 'favorite_number.json'

try:
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)
except FileNotFoundError:
    print("Sorry, " + filename + " doesnot exit.")
else:
    print("I know your favorite number! It's " + str(favorite_number)+ ".")
