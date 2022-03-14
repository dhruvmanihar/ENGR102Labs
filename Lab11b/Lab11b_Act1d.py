# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 11b_Act1d
# Date: 11/27/2021


#partd function
# doc = open('C:/Users/dhruv/Desktop/Intro to Engineering/Python/CLLWeatherData.csv', 'r')
import csv
def partd(filename):
    csv.writer(open('test.tsv', 'w+'), delimiter='\t').writerows(csv.reader(open(filename)))
    return 'Done!'




