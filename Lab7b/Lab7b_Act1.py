# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 7b_Act1
# Date: 10/18/2021

name = input("What is your name? ")

x = name
y = ""

#if else block to determine where vowels are in string
#based on where they are, the string will slice

if name[0] == "A" or name[0] == "E" or name[0] == "I" or name[0] == "O" or name[0] == "U":

    y = name[0].lower() + name[1:]

elif name[1] == "a" or name[1] == "e" or name[1] == "i" or name[1] == "o" or name[1] == "u":

    y = name[1:]

else:

    y = name[2:]


#prints rhyme scheme to console
print (x, x, "Bo-B"+y, sep = ", ")
print ("Banana-Fana Fo-F"+y)
print ("Me Mi Mo-M"+y)
print (x+"!")








