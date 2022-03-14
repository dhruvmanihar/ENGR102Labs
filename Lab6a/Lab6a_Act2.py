# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 6a_2
# Date:         10 9 2021
#


lower = 2
upper = 100
num_prime = 0
for num in range(lower,upper + 1):
    #all prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0: #divisible by i
                print(num,"is not prime")
                break
        else: #not divisible by i
            num_prime += 1
            print(num,"is prime")
print("There are",num_prime," prime numbers between 2 and 100")
