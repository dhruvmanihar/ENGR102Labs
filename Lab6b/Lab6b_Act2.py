# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 6b_Act2
# Date: 10/13/2021


#initial input
userin = int(input("Enter an integer: "))
sum = 0
product = 1

for i in range (userin+1):

    sum += i
    if i < userin:
        product *= i+1


if userin == 0:
    sum = 0
    product = 0

#final print statements
print ("The sum of all integers from 0 to", userin, "is", sum)
print ("The product of all integers from 1 to", userin, "is", product)
