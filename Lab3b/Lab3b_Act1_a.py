# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 3b_Act1_a
# Date: 09/16/2021

from math import *

#A: This program calculates the applied force given mass and acceleration

print("This program calculates the applied force given mass and acceleration")
object_mass = float(input("Please enter the mass (kg): "))
object_acceleration = float(input("Please enter the acceleration (m/s^2): "))
object_force = object_mass*object_acceleration
print("Force is {:.1f} N".format(object_force))
