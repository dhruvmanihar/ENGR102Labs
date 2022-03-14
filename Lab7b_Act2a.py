# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 7b_Act2a
# Date: 10/18/2021



stringin = input("Enter three or more prices separated by spaces: ")

listin = []

#converts string to list
for i in stringin.split(" "):
    listin.append(float(i))

#loops through list to print
for i in range(len(listin)):
    x = (listin[i])
    print("$"+"{:.2f}".format(x).rjust(7))

