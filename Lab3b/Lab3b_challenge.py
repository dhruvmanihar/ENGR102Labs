# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 3b_challenge
# Date: 09/18/2021

#Calculates pi digits based on user input

from math import *

precision = int(input("Please enter the number of digits of precision for pi: "))

str_pi = "{num_pi:." + str(precision)+ "f}"
finalpi = str_pi.format(num_pi = pi)

final_string = "The value of pi to "+ str(precision) + " digits is: " + finalpi
#finalpi = ("{:.",precision,"f}").format(pi)


print(final_string)

