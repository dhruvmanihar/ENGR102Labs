# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 3b_Act1_b
# Date: 09/16/2021

from math import *

#B: This program calculates the wavelength given distance and angle

print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))



wavelength = 2*distance*sin(radians(angle))
print("Wavelength is {:.4f} nm".format(wavelength))