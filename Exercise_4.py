# Exercise 4: Ask the user for a circle radius to calcute its area.

from cmath import pi

r = float(input('Write the radius in meters: '))

area = pi * r ** 2

print('The circle area is {}'.format(area))