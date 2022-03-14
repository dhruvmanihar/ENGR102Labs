# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 7b_Act3
# Date: 10/18/2021

from math import *

#input elements for each vector
a_in = input("Enter the elements for vector A: ")
b_in = input("Enter the elements for vector B: ")

new_a = []
new_b = []

#split function helps seperate individual vector values and append to new list
for i in a_in.split(" "):
    new_a.append(float(i))

for i in b_in.split(" "):
    new_b.append(float(i))

#define magnitude vairables
a_mag = 0
b_mag = 0

#calculate magnitude through loops
for i in range (len(new_a)):
    a_mag += (new_a[i])**2

for i in range (len(new_b)):
    b_mag += (new_b[i])**2

a_mag = sqrt(a_mag)
b_mag = sqrt(b_mag)


#create empty lists for addition, subtraction and new var for dot product
add = []
sub = []
dot = 0

#loop through list and calculate each variable
for i in range (len(new_a)):

    a = float(new_a[i] + new_b[i])
    s = float(new_a[i] - new_b[i])
    add.append(a)
    sub.append(s)

    dot += new_a[i] * new_b[i]

#print statements
print ("The magnitude of vector A is {:.4f}".format(a_mag))
print ("The magnitude of vector B is {:.4f}".format(b_mag))
print ("A + B is", add)
print ("A - B is", sub)
print ("The dot product is", float(dot))

