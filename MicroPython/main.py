"""
Created by: Jet Lu
Created on: Feb 2026
This module is a Micro:bit MicroPython program that can perform basic math
"""

from microbit import *

sleep(1000)

# Dimensions
display.scroll("A rectangle has dimensions 5 cm & 3 cm")

# Perimeter
display.scroll("The perimeter: 2(5+3)=" + (2 * (5 + 3)) + " cm")

# Area
display.scroll("The area: 5x3 =" + (5 * 3) + " cm^2")
