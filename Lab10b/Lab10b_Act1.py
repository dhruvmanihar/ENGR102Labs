# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 10b_Act1
# Date: 11/17/2021


#import numpy module and matplotlib
import numpy as numpy
import matplotlib.pyplot as plt

#numpy array for points
spiral = numpy.array([(1.0),(0.0)])

#multiply constant matricies so that each numpy get multiplied
constant = numpy.array([(1.00583,-0.087156),(0.07156, 1.00583)])

#initialize count
count = 1

#multiply starting numpy by the constant matrix
p = constant.dot(spiral)

#create two lists for x and y
x = [1.0]
y = [0.0]

#loop to calculate vector
while count < 250:
    p = constant.dot(p)
    x.append(p[0])
    y.append(p[1])
    count += 1

plt.scatter(x,y)
plt.xlabel('x-component')
plt.ylabel('y-component')
plt.suptitle('outward growing spiral')
