#!/usr/bin/env python3

def get_city_country(city, country):
	city_in_country = city.title() + ', ' + country.title()
	return city_in_country
	
city_c1 = get_city_country('beijing', 'china')
city_c2 = get_city_country('shanghai', 'china')
city_c3 = get_city_country('nanjing', 'china')
print(city_c1 + "\n" + city_c2 + "\n" + city_c3 )
