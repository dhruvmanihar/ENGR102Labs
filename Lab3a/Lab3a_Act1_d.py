# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 3a_1d
# Date:         09 15 2021
#


from math import *
#user input
watts = float(input("Please enter the number of watts to be converted to BTU per hour: "))

BTU_hr = watts * 3.412141633

#final print
print('{:.2f} watts is equivalent to {:.2f} BTU per hour'.format(watts,BTU_hr))
