#!/usr/bin/env python3

def describe_city(city, country='china'):
	print(city.title() + "is in " + country.title())

describe_city('shanghai')
describe_city('beijing')
describe_city('reykjavik', 'iceland')
