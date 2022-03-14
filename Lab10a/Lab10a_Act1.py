# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 10a_1
# Date:         11 15 2021
#
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material


#import numpy module
import numpy as np

#using arrange and reshape to create 3x4 matrix with increasing increments
a = np.arange(12).reshape(3, 4)
print("A =",a)

print("")

b = np.arange(8).reshape(4,2)
print ("B =",b)

print("")

c = np.arange(6).reshape(2,3)
print ("C =",c)

#matrix multiplication using @
d = a@b@c

print("")

print ("D =",d)

print("")

#transpose matrix using .T
dt = d.T

print ("D^T =",dt)

print ("")

e = (d)**(1/2) / 2

print ("E =",e)









