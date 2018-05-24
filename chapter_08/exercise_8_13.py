#!/usr/bin/env python3

def build_profile(first, last, **user_info):
	"""create a dictionary inclding everything about the users"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('ke', 'jie', 
								location = 'shanghai',
								field='physics')

print(user_profile)
	
