# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 6b_Act1
# Date: 10/13/2021


#assign variables
i = 0
userin = int(input("Enter a positive integer to compute the Collatz sequence: "))

#initial print statments
print("Here is the Collatz sequence starting at {:.0f}:".format(userin))

if userin == 1:
    print (1)
    print ("It took", i, "iterations to reach 1")
else:
    print(userin,end=", ")

    #while loop and print for sequence
    while userin > 1:

        if userin % 2 == 0:
            userin /= 2
        else:
            userin = 3*userin + 1

        userin = int(userin)

        if userin == 1:
            print(userin)
        else:
            print (userin,end = ", ")

        i += 1

    print ("It took", i, "iterations to reach 1")