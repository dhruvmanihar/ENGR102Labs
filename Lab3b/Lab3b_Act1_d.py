# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 3b_Act1_d
# Date: 09/16/2021

from math import *
# This program calculates the pressure given moles, volume, and temperature

print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
temp = float(input("Please enter the temperature (K): "))
gas_constant = 8.314

pressure = (moles*temp*gas_constant)/(volume*1000)
print("Pressure is {:.0f} kPa".format(pressure))