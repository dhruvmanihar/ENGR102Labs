# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 4b_Act1
# Date: 09/22/2021


num1=float(input("Enter number 1: "))
num2=float(input("Enter number 2: "))
num3=float(input("Enter number 3: "))
if(num1<=num2):
      if(num1<=num3):
            Smallest=num1
      else:
          Smallest=num3
else:
      if (num2<=num3):
        Smallest=num2
      else:
        Smallest=num3
        #display the smallest number
print("The smallest number is", Smallest)

