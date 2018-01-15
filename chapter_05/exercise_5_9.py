names = ['admin', 'b', 'c', 'd', 'e']
for name in names:
	if name == 'admin':
		print("Hello, admin, would you like to see a status report?")
	else:
		print("Hello " + name + ", thank you for logging in again")

if names:
	print("We need to find some users!")

