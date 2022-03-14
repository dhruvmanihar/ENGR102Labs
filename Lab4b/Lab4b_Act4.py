# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 4b_Act4
# Date: 09/22/2021

from math import *

#enter coefficients

a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

#calculate dsicriminant

disc = (b**2) - (4*a*c)

#for invalid coefficients

if a == 0 and b == 0:
    print("You entered an invalid combination of coefficients")
    exit()

#assign variables

root_count = 0
root = 0
root1 = 0
root2 = 0
linroot = 0

#if else conditions to determine roots

if a == 0 and b != 0:
    linroot = (-c) / b
else:
    if disc == 0:
        root_count = 1
    elif disc > 0 or disc < 0:
        root_count = 2
    elif a == 0 and b == 0:
        root_count == 0

if root_count == 1:
    root = (-b) / (2 * a)
elif disc > 0 and root_count == 2:
    root1 = ((-b) + (sqrt((b**2) - (4*a*c)))) / (2 * a)
    root2 = ((-b) - (sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
elif disc < 0 and root_count == 2:
    p1 = -b / (2 * a)
    i1 = (sqrt( (abs (((b**2) - (4*a*c)))))) / 2
    p2 = str (i1) + "i"
    root1 = str(p1) + " + " + p2
    root2 = str(p1) + " - " + p2

#if else conditions to print correctly

if a == 0 and b == 0:
    print("You entered an invalid combination of coefficients")
elif a == 0:
    print ("The root is x =", linroot)
else:
    if root_count == 1:
        print("The root is x =", root)
    elif root_count == 2:
        print("The roots are x =", root1, "and x =", root2)