# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 3b_Act2
# Date: 09/18/2021

#Given area calculates radius/side length of vairous shapes

from math import *

area = float(input("Please enter the area: "))

def radCircle (area):
    radius = sqrt(area/pi)
    print("A circle with area {:.2f} has a radius {:.3f}".format(area, radius))

def sideTri (area):
    side = sqrt(area/((sqrt(3)/4)))
    print("An equilateral triangle with area {:.2f} has a side {:.3f}".format(area, side))

def sideSquare (area):
    side = sqrt(area)
    print("A square with area {:.2f} has a side {:.3f}".format(area, side))

def sidePent (area):
    #side = (area)/((.25)*(sqrt(5*(5+2*sqrt(5)))))
    side = 2 * (5 ** (3 / 4)) * ((sqrt(area)) / (5 * ((sqrt(20) + 5)) ** (1 / 4)))
    print("A pentagon with area {:.2f} has a side {:.3f}".format(area, side))

def sideDodeca (area):
    side = sqrt(area/(3 * (2+sqrt(3))))
    print("A dodecagon with area {:.2f} has a side {:.3f}".format(area, side))

radCircle (area)
sideTri (area)
sideSquare (area)
sidePent (area)
sideDodeca (area)