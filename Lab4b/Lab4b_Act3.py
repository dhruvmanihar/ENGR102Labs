# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 4b_Act3
# Date: 09/22/2021

#formula: .5*day**2 + .5*day + 45

#input from user
day = int(input("Please enter a positive value for day: "))
widgets = 0

#if else block for invalid staements/calculations
if day < 0:
    print("You entered an invalid number!")
    exit()
elif day <= 10:
    widgets = day * 10
elif day < 50:
    widgets = .5*day**2 + .5*day + 45
elif day < 101:
    widgets = (.5*49**2 + .5*49 + 45) + ((day-49) * 50)
else:
    widgets = 3820

#conversion to int and final print statment
widgets = int(widgets)
print("The total number of widgets produced on day", day, "is", widgets)