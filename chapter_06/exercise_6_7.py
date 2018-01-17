information1 = {
	'first_name':'Jie', 
	'last_name':'Ke',
	'age':27,
	'city':'shanghai',
	}

information2 = {
	'first_name':'Yiyu', 
	'last_name':'Ke',
	'age':0,
	'city':'shanghai',
	}
	
information3 = {
	'first_name':'Yi', 
	'last_name':'Ke',
	'age':0,
	'city':'shanghai',
	}	
	
people = [information1, information2, information3]

for man in people:
	print("\n" + str(man))
	for key, value in man.items():
		print("\nKey:" + key)
		print("Value: " + str(value))
