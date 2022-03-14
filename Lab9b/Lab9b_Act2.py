# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 9b_Act2
# Date: 11/11/2021

#inputs
file_n = input("Please enter the output filename: ")
price = int(input("Please enter the principal amount: "))
length = int(input("Please enter the term length (months): "))
interest = float(input("Please enter the annual interest rate: "))

#payment equation
payment = (price*(interest/12))/(1-((1/(1+(interest/12)))**length))

file = open(file_n, "w")

total_loan_interest = 0
for i in range(length + 1 ):
    file.write("{},${:.2f},${:.2f},\n".format(i,total_loan_interest,price))
    count_loan_int = price*(interest/12)
    total_loan_interest += price*(interest/12)
    price = price - (payment-count_loan_int)

file.close()
