# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 4a_2
# Date:         09 24 2021
#

from math import *


#user inputs

a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

# assign signs to variables

if a < 0:
    s1 = "-"
else:
    s1 = ""

if b < 0:
    s2 = "-"
elif b > 0:
    s2 = "+"
else:
    s2 = ""

if c < 0:
    s3 = "-"
elif c > 0:
    s3 = "+"
else:
    s3 = ""

#assign numbers to variables

if a > 1 or a < -1:
    n1 = str(abs(a))+"x^2"
elif a == 0:
    n1 = ""
else:
    n1 = "x^2"

if b > 1 or b < -1:
    n2 = str(abs(b))+"x"
elif b == 0:
    n2 = ""
else:
    n2 = "x"

n3 = abs(c)

#print statements

if a == 0:
    if b >= 1:
        s2 = ""
    print("The quadratic equation is", n2, s3, n3, "= 0")
elif b == 0:
    print("The quadratic equation is", n1, s3, n3, "= 0")
elif c == 0:
    print("The quadratic equation is", n1, s2, n2, "= 0")
else:
    if a >= 1:
        print("The quadratic equation is", n1, s2, n2, s3, n3, "= 0")
    else:
        print("The quadratic equation is", s1, n1, s2, n2, s3, n3, "= 0")


