#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment6 - Refactoring Test.  Tested in Python 2.7.15"""

import unittest

class ConversionNotPossible(Exception):
    pass

distance = {
            'met': {'yar':(0,1.09361,0),
                    'mil':(0,0.000621371,0)},
            'yar': {'mil':(0,0.000568182,0),
                    'met':(0,0.9144,0)},
            'mil': {'met':(0,1609.34,0),
                    'yar':(0,1760,0)}
            }
temperature = {
                'kel':{'cel':(0,1,-273.15),
                    'fah':(-273.15,1.80,32)},
                'cel':{'kel':(0,1,273.15),
                   'fah':(0,1.80,32)},
                'fah':{'kel':(-32,0.5556,273.15),
                   'cel':(-32,0.5556,0)}
              }

def convert(fromUnit, toUnit, value):
    """Function to convert fromUnit to toUnit"""
    fromUnit = fromUnit[0:3]
    toUnit = toUnit[0:3]
    if not ((fromUnit in distance and toUnit in distance
             ) or (fromUnit in temperature and toUnit in temperature)):
        raise ConversionNotPossible
    else:
        if fromUnit == toUnit:
            my_convert = value
        elif fromUnit in distance:
            my_convert = (
                (value + distance[fromUnit][toUnit][0])
                * distance[fromUnit][toUnit][1]
                + distance[fromUnit][toUnit][2]
                )
        else:
            my_convert = (
                (value + temperature[fromUnit][toUnit][0])
                * temperature[fromUnit][toUnit][1]
                + temperature[fromUnit][toUnit][2])

    return float("%0.2f" %my_convert)


class ConvertTests(unittest.TestCase):

    def testTemperature(self):
        self.assertEqual(convert('kelvin','fahrenheit',0),-459.67)
        self.assertEqual(convert('kelvin','celsius',0),-273.15)
        self.assertEqual(convert('celsius','fahrenheit',0),32.0)
        self.assertEqual(convert('celsius','kelvin',0),273.15)
        self.assertEqual(convert('fahrenheit','celsius',0),-17.78)
        self.assertEqual(convert('fahrenheit','kelvin',0),255.37)

    def testDistance(self):
        self.assertEqual(convert('mile','meter',100),160934.0)
        self.assertEqual(convert('mile','yard',100),176000.0)
        self.assertEqual(convert('meter','mile',100),0.06)
        self.assertEqual(convert('meter','yard',100),109.36)
        self.assertEqual(convert('yard','meter',100),91.44)
        self.assertEqual(convert('yard','mile',100),0.06)

    def testSelfTest(self):
        for my_test in distance:
            self.assertEqual(convert(my_test, my_test, 10), 10)
        for my_test in temperature:
            self.assertEqual(convert(my_test, my_test, 10), 10)

    def testIncompatible(self):
        self.assertRaises(ConversionNotPossible,convert,'met','cel',0)

if __name__ == '__main__':
    unittest.main()
