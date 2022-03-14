# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 7b_Act2b
# Date: 10/18/2021


#input values from user
stringin = input("Enter three or more values separated by spaces: ")
seperator = input("Enter a two-character separator: ")


listin = []

#converts string into list
for i in stringin.split(" "):
    listin.append(float(i))


#loops through list to print
for i in range(len(listin)):
    x = ((listin[i]))
    y = " " + seperator + " "

    if i != (len(listin) - 1):
        print(x, end = y)
    else:
        print (x)