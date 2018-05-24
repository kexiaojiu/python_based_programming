#!/usr/bin/env python3

def make_car(maker, size, **car_info):
	car = {}
	car['maker'] = maker
	car['size'] = size
	
	for key, value in car_info.items():
		car[key] = value
	return car
	
car_profile = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car_profile)	
