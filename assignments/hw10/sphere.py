"""
Name: <Steve Hyland>
HW10.py

Problem: Sphere class

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
# sphere.py
# contains the class sphere
#
import math
# define the class
class Sphere:
    ''' Defines the class'''
#
# now define the instance methods
    def __init__(self, radius):
        ''' initialize the radius'''
        self.radius = radius
#
    def get_radius(self):
        ''' return the radius'''
        return self.radius
#
    def surface_area(self):
        ''' return the surface area'''
        return 4 * math.pi * self.radius ** 2
#
    def volume(self):
        ''' return the volume'''
        return 4/3 * math.pi * self.radius ** 3
#
