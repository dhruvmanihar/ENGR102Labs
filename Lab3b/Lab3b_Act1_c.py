# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 3b_Act1_c
# Date: 09/16/2021

from math import *

#C: Calculate calculates how much Radon-222 is left given time and initial amount

print("This program calculates how much Radon-222 is left given time and initial amount")
time = float(input("Please enter the time (days): "))
initialAmount = float(input("Please enter the initial amount (g): "))
halfLife = 3.8
elementLeft = initialAmount*(2**(-time/halfLife))
print("Radon-222 left is {:.2f} g".format(elementLeft))
