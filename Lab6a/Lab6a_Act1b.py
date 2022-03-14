# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 6a_1b
# Date:         10 9 2021
#


from math import *

#input side length and layers

side_length = float(input("Enter the side length in meters: "))
layers = float(input("Enter the number of layers: "))


side_layers = layers * 4
total_sides = (layers *(4 + side_layers)) / 2
top_sa = (side_length * layers)**2
side_sa = (side_length**2) * total_sides
total_area = top_sa + side_sa


print("You need", "{:.2f}".format(total_area), "square meters of gold foil to cover the pyramid")
