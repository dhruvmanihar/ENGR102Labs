# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 3a_1f
# Date:         09 15 2021
#
#user input
celsius = float(input("Please enter the number of degrees Celsius to be converted to degrees Rankine: "))

rankine = (9/5) * celsius + 491.67

#final print
print("{:.2f} degrees Celsius is equivalent to {:.2f} degrees Rankine".format(celsius,rankine))
