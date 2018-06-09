#!/usr/bin/env python3
"""test employee class"""
import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee('Jie', 'Ke', 300000)
        
    def test_give_default_raise(self):
        self.employee1.give_raise()
        self.assertEqual(self.employee1.annual_salary, 305000)
        
    def test_give_custom_raise(self):
        self.employee1.give_raise(10000)
        self.assertEqual(self.employee1.annual_salary, 310000)
    
    
unittest.main()
