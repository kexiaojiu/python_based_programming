cities = {
	'Shanghai':{'country':'China', 'population': 20000000, 'fact':'east of china'},
	'Beijing':{'country':'China', 'population': 3000000, 'fact':'north of china'},
	'Shenzhen':{'country':'China', 'population': 10000000, 'fact':'south of china'},
	}

for city, city_info in cities.items():
	print("\nCity: " + city)
	print("\tcountry: " + city_info['country'])
	print('\tpopulation: ' + str(city_info['population']))
	print('\tfact:' + city_info['fact'])
