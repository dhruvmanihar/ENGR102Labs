# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 6a_1a
# Date:         10 9 2021
#


#input statements
c_length = float(input("Enter the side length in meters: "))
layer = int(input("Enter the number of layers: "))

side_area = 0
top_area = 0

for layers in range(layer):
    layers += 1

    top_area += (c_length * layers) ** 2 - (c_length * (layers - 1)) ** 2

    side_area += (c_length ** 2) * (4 * layers)

total_area = side_area + top_area
print("You need", "{:.2f}".format(total_area), "square meters of gold foil to cover the pyramid")
