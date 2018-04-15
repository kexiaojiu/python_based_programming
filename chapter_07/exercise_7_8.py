#!/usr/bin/env python3

sandwich_orders = ['sandwich001', 'sandwich002', 'sandwich003']

finished_sandwiches = []

while sandwich_orders:
	sandwich_order = sandwich_orders.pop()
	
	print("I made your " + sandwich_order + " sandwich.")
	finished_sandwiches.append(sandwich_order)

print("\n--- The following sandwiches have been finished ---")
for finished_sandwiche in finished_sandwiches:
	print(finished_sandwiche)
