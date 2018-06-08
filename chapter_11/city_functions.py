#!/usr/bin/env python3

    
def city_country(city,  country, population=0):
    """Generate a neatly formatted full city&country"""
    if population == 0:
        full_city_country = city.title() + ', ' + country.title()
    else:
        full_city_country = city.title() + ', ' + country.title() + " - population " + str(population)
        
    return full_city_country
