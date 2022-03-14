# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 4a_1
# Date:         09 24 2021
#



from math import *

#initial print statement

print("Enter the hours parked as a decimal number. Include a negative sign if the ticket is lost.")
user_hours = float(input("Please enter the hours parked: "))
hours_parked = user_hours

#if for ticket lost

ticket_lost = False
if hours_parked < 0:
    ticket_lost = True
    hours_parked *= -1

hours_parked = ceil(hours_parked)
days = int(hours_parked / 24)
added_hours = int(hours_parked % 24)
charges = 0

#if statements for charges

if added_hours > 0:
    charges += 4
if added_hours > 2:
    charges += 3
if added_hours > 4:
    charges += (added_hours - 4)
if charges > 24:
    charges = 24
if ticket_lost:
    charges += 36

charges += (days * 24)
print("Parking for", user_hours, "hours please pay $" + str(charges))

