# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 11b_Act1e
# Date: 11/27/2021

#import median from numpy
from numpy import median


def parte (initialList):

    #sort method sorts by ascending order
    initialList.sort()
    min = initialList[0]
    max = initialList[len(initialList)-1]
    #uses median method to find median in list
    med = median(initialList)
    return min, med, max


