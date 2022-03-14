# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 3a_1c
# Date:         09 15 2021
#

#user input
atmospheres = float(input("Please enter the number of atmospheres to be converted to millimeters of mercury: "))

mercury = 760 * atmospheres

#final print
print("{:.2f} atmospheres is equivalent to {:.2f} millimeters of mercury".format(atmospheres, mercury))