# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 5b_Act2
# Date: 10/04/2021

import sys

# y = (slope)(x-x1)+y1

# Setting Values for A,C,D,E

x1 = 0.01
y1 = 43

x2 = 0.06
y2 = 43.5

x3 = 0.18
y3 = 60

x4 = 0.27
y4 = 51

# User Input
x = float(input("Enter the strain: "))

# Checking Strain Input
if x < 0 or x > x4:
    print("Strain is undefined in that region")
    sys.exit()

if x > 0 and x < x1:
    y = ((y1 - 0) / (x1 - 0)) * (x - 0) + 0

if x > x1 and x < x2:
    y = ((y2 - y1) / (x2 - x1)) * (x - x1) + y1

if x > x2 and x < x3:
    y = ((y3 - y2) / (x3 - x2)) * (x - x2) + y2

if x > x3 and x < x4:
    y = ((y4 - y3) / (x4 - x3)) * (x - x3) + y3

# Special Cases

if x == 0:
    y = 0

if x == x1:
    y = y1

if x == x2:
    y = y2

if x == x3:
    y = y3

if x == x4:
    y = y4

# Output
print("The stress is approximately {:3.1f}".format(y))
