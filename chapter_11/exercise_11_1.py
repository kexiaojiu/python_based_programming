#!/usr/bin/env python3
"""test city functions"""

import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        full_city_country = city_country('santiago', 'chile')
        self.assertEqual(full_city_country, 'Santiago, Chile')

unittest.main()
