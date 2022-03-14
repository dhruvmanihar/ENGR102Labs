
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 2a_3
# Date:         10 10 2021
#

from math import *

#part 1

t0 = 10
t1 = 55
x0 = 2025
x1 = 23025
given_t = 25
x = ((x1-x0)/(t1-t0))*(given_t-t1)+x1
print("Part 1:\nFor t =", given_t,"minutes, the position p =", x, "kilometers")

#part 2

t0 = 10
t1 = 55
x0 = 2025
x1 = 23025
given_t = 5*60
radius = 6745
circumfrence = 2 * radius * pi
x = (((x1-x0)/(t1-t0))*(given_t-t1)+x1) - (3 * circumfrence)
print("Part 2:\nFor t =", 5.0,"hours, the position p =", x, "kilometers")
