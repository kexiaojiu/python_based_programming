#!/usr/bin/env python3

sandwich_orders = ['pastrami', 'sandwich002', 'sandwich003', 'pastrami', 'pastrami']


print("Sorry, the pastrami has been selt out.\n")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print(sandwich_orders)

