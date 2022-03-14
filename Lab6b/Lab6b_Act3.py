# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 6b_Act3
# Date: 10/13/2021

numin = int(input("Enter a four-digit integer: "))
num = numin
iterations = 0

print(num, end='')

while num != 6174 or num != 0:

    num1 = str((int(num // 1000) % 10))
    num2 = str((int(num // 100) % 10))
    num3 = str((int(num // 10) % 10))
    num4 = str((num % 10))

    large = ""
    small = ""

    # for loop to reorder numbers
    for i in range(4):
        large += max(num1, num2, num3, num4)
        small = max(num1, num2, num3, num4) + small
        if max(num1, num2, num3, num4) == num1:
            num1 = '/'
        elif max(num1, num2, num3, num4) == num2:
            num2 = '/'
        elif max(num1, num2, num3, num4) == num3:
            num3 = '/'
        else:
            num4 = '/'

    if num == 1111 or num == 2222 or num == 3333 or num == 4444 or num == 5555 or num == 6666 or num == 7777 or num == 8888 or num == 9999:
        num = 0000
        iterations = 1
        print(' > ' + "0",end = "")
        break


    num = int(large) - int(small)
    print(' > ' + str(num), end='')

    iterations += 1

    if num == 6174:
        break



print()

print(numin, "reaches", num, "via Kaprekar's routine in", iterations, "iterations")

