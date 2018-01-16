rivers = {
	'Nile': 'Egypt',
	'Amazon': 'Brasil',
	'Changjiang':'China',
	}

for river, country in rivers.items():
	print("The " + river + " runs through " + country + ".\n")
	
print("\nThe names of the three rivers are: ")
for river in rivers.keys():
	print(river)

print("\nThe countries of the three rivers are: ")
for country in rivers.values():
	print(country)
