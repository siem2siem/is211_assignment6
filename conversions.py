#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment6 - Temperature Conversion.  Tested in Python 2.7.15"""

def convertCelsiusToKelvin(temperature):
    """
    Function takes in a value representing a Celsius measurement,
	and returns that temperature converted into Kelvin.
    Args:
        temperature(float): Float value used for conversion
    Return:
	    Value representing Kelvin measurements
    Example:
        >>> convertCelsiusToKelvin(300)
        573.15
    """
    my_temp = temperature + 273.15
    return float("%.3f" % my_temp)


def convertCelsiusToFahrenheit(temperature):
    """
    Function takes in a value representing a Celsius measurement,
	and returns that temperature converted into Fahrenheit
    Args:
        temperature(float): Float value used for conversion
    Return:
	    Value representing Fahrenheit measurements
    Example:
        >>> convertCelsiusToFarenheit(300)
        572.0
    """
    my_temp = (1.8 * temperature) + 32
    return float("%.3f" % my_temp)


def convertFahrenheitToKelvin(temperature):
    """
	Takes in a float representing a Fahrenheit measurement,
	and returns that temperature converted into Kelvin.
    Args:
        temperature(float): Float value used for conversion
    Return:
	    Value representing Kelvin measurements
    Example:
        >>> convertFahrenheitToKelvin(300)
        422.039
    """
    my_temp = ((temperature - 32) / 1.8) + 273.15
    return float("%.3f" % my_temp)


def convertFahrenheitToCelsius(temperature):
    """
    Function takes in a float representing a Fahrenheit measurement,
	and returns that temperature converted into Celsius
    Args:
        temperature(float): Float value used for conversion
    Return:
	    Value representing Celsius measurements
    Example:
        >>> convertFahrenheitToCelsius(300)
    148.889
    """
    my_temp = (temperature - 32) / 1.8
    return float("%.3f" % my_temp)


def convertKelvinToCelsius(temperature):
    """
    Function takes in a float representing a Kelvin measurement,
	and returns that temperature converted into Celsius
    Args:
        temperature(float): Float value used for conversion
    Return:
	    Value representing Celsius measurements
    Example:
        >>> convertKelvinToCelsius(300)
    26.85
    """
    my_temp = temperature - 273.15
    return float("%.3f" % my_temp)


def convertKelvinToFahrenheit(temperature):
    """
    Function takes in a float representing a Kelvin measurement,
	and returns that temperature converted into Fahrenheit
    Args:
        temperature(float): Float value used for conversion
    Return:
	    Value representing Fahrenheit measurements
    Example:
        >>> convertKelvinToFahrenheit(300)
    80.33
    """
    my_temp = (temperature - 273.15) * 1.8 + 32
    return float("%.3f" % my_temp)
