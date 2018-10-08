#! usr/bin/env python
# *-* coding: utf-8 *-*
"""IS211 Assignment6 - Unit Test.  Tested in Python 2.7.15"""

import conversions
import unittest

class CelsiusToKelvin(unittest.TestCase):


    def test_zero_input(self):
        "Function test with zero as input."
        results = conversions.convertCelsiusToKelvin(0)
        self.assertEqual(273.15, results)


    def test_positive_input(self):
        "Function test with positive integer input."
        results = conversions.convertCelsiusToKelvin(300)
        self.assertEqual(573.15, results)


    def test_negative_input(self):
        "Function test with negative integer input."
        results = conversions.convertCelsiusToKelvin(-10)
        self.assertEqual(263.15, results)


    def test_float_input(self):
        "Function test with float as input."
        results = conversions.convertCelsiusToKelvin(10.10)
        self.assertEqual(283.25, results)


    def test_large_input(self):
        "Test for large input."
        results = conversions.convertCelsiusToKelvin(10000)
        self.assertEqual(10273.15, results)

		
class CelsiusToFahrenheit(unittest.TestCase):


    def test_zero_input(self):
        "Function test with zero as input."
        results = conversions.convertCelsiusToFahrenheit(0)
        self.assertEqual(32.0, results)


    def test_positive_input(self):
        "Function test with positive integer input."
        results = conversions.convertCelsiusToFahrenheit(300)
        self.assertEqual(572.0, results)


    def test_negative_input(self):
        "Function test with negative integer input."
        results = conversions.convertCelsiusToFahrenheit(-10)
        self.assertEqual(14, results)


    def test_float_input(self):
        "Function test with float as input."
        results = conversions.convertCelsiusToFahrenheit(10.10)
        self.assertEquals(50.18, results)


    def test_large_input(self):
		"Function test with a large integer."
		results = conversions.convertCelsiusToFahrenheit(10000)
		self.assertEqual(18032.0, results)


class FahrenheitToKelvin(unittest.TestCase):


    def test_zero_input(self):
        "Function test with zero as input."
        results = conversions.convertFahrenheitToKelvin(0)
        self.assertEqual(255.372, results)


    def test_positive_input(self):
        "Function test with positive integer input."
        results = conversions.convertFahrenheitToKelvin(300)
        self.assertEqual(422.039, results)


    def test_negative_input(self):
        "Function test with negative integer input."
        results = conversions.convertFahrenheitToKelvin(-10)
        self.assertEqual(249.817, results)


    def test_float_input(self):
        "Function test with float as input."
        results = conversions.convertFahrenheitToKelvin(10.10)
        self.assertEqual(260.983, results)


    def test_large_input(self):
		"Function test with a large integer."
		results = conversions.convertFahrenheitToKelvin(10000)
		self.assertEqual(5810.928, results)

		
class FahrenheitToCelsius(unittest.TestCase):


    def test_zero_input(self):
        "Function test with zero as input."
        results = conversions.convertFahrenheitToCelsius(0)
        self.assertEqual(-17.778, results)


    def test_positive_input(self):
        "Function test with positive integer input."
        results = conversions.convertFahrenheitToCelsius(300)
        self.assertEqual(148.889, results)


    def test_negative_input(self):
        "Function test with negative integer input."
        results = conversions.convertFahrenheitToCelsius(-10)
        self.assertEqual(-23.333, results)
 

    def test_float_input(self):
        "Function test with float as input."
        results = conversions.convertFahrenheitToCelsius(10.10)
        self.assertEqual(-12.167, results)


    def test_large_input(self):
		"Function test with a large integer."
		results = conversions.convertFahrenheitToCelsius(10000)
		self.assertEqual(5537.778, results)


class KelvinToCelsius(unittest.TestCase):


    def test_zero_input(self):
		"Function test with zero as input."
		results = conversions.convertKelvinToCelsius(0)
		self.assertEqual(-273.15, results)


    def test_positive_input(self):
		"Function test with positive integer input."
		results = conversions.convertKelvinToCelsius(300)
		self.assertEqual(26.85, results)


    def test_negative_input(self):
		"Function test with negative integer input."
		results = conversions.convertKelvinToCelsius(-10)
		self.assertEqual(-283.15, results)


    def test_float_input(self):
		"Function test with float as input."
		results = conversions.convertKelvinToCelsius(10.10)
		self.assertEqual(-263.05, results)


    def test_large_input(self):
		"Function test with a large integer."
		results = conversions.convertKelvinToCelsius(10000)
		self.assertEqual(9726.85, results)

		
class KelvinToFahrenheit(unittest.TestCase):


    def test_zero_input(self):
		"Function test with zero as input."
		results = conversions.convertKelvinToFahrenheit(0)
		self.assertEqual(-459.67, results)	

		
    def test_positive_input(self):
        "Function test with positive integer input."
        results = conversions.convertKelvinToFahrenheit(300)
        self.assertEqual(80.33, results)

		
    def test_negative_input(self):
        "Function test with negative integer input."
        results = conversions.convertKelvinToFahrenheit(-10)
        self.assertEqual(-477.67, results)

		
    def test_float_input(self):
        "Function test with float as input."
        results = conversions.convertKelvinToFahrenheit(10.10)
        self.assertEqual(-441.49, results)


    def test_large_input(self):
		"Function test with a large integer."
		results = conversions.convertKelvinToFahrenheit(10000)
		self.assertEqual(17540.33, results)


if __name__ == "__main__":
    unittest.main()
