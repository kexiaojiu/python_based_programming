pizzas = ['pizza1', 'pizza2', 'pizza3']

friends_pizzas = pizzas[:]
pizzas.append('apple')
friends_pizzas.append('orange')
print("My favorite pizza are:")
for pizza in pizzas:
	print(pizza)
	
print("\nMy friend's 'favorite pizza are:")
for pizza in friends_pizzas:
	print(pizza)
	
	

