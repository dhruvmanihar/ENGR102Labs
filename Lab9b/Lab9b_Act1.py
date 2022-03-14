# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 9b_Act1
# Date: 11/11/2021


#intialize variables
count = 0
total = 0

#open files
myGame = open("game.txt", "r")
myCoins = open("coins.txt", "w")
line = myGame.readlines()
while count < len(line):
    command = line[count]
    if "coin" in line[count]:
        if command[5] == "+":
            total += int(command[6:])
            count += 1
            myCoins.write("{} \n".format(command[6:]))
        if command[5] == "-":
            total -= int(command[6:])
            count += 1
            myCoins.write("{} \n".format(command[6:]))
    elif "jump" in line[count]:
        if command[5] == "+":
            count += int(command[6:])
        if command[5] == "-":
            count -= int(command[6:])
    elif "none" in line[count]:
        count += 1
    else:
        count += 1

myGame.close()
myCoins.close()
print("Total coins:", total)
