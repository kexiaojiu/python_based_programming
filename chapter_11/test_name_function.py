#!/usr/bin/env python3
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """test name_function.py"""
    
    def test_first_last_name(self):
        """Can it deal with the name such as Janis Joplin?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
    def test_first_middle_last_name(self):
        """Can it deal with the name such as Wolfgang Amadeus Mozart"""
        formatted_name = get_formatted_name('wolfgang', 'mozart','amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
        
unittest.main()
