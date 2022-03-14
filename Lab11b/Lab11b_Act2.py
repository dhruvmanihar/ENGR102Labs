# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 11b_Act2
# Date: 11/27/2021

import random
def getRandom():
    # return the random number in given range
    return random.randint(1,100)
#returns 0 if matches
#returns +number if it is greater
#returns -number if it is lower
def getResult(randomNumber,guess):
        return guess-randomNumber

def main():
  #getting random number
        randomNumber = getRandom()
        count=0
        print("Guess the secret number! Hint: It's an integer between 1 and 100")
  #loop until user give correct number
        while(True):
                guess = int(input("What is your guess?"))
                count+=1
                dec=getResult(randomNumber,guess)
                if dec==0:
                        print("You guessed it! it took you ",count,"guesses.")
                        break
                elif dec>0:
                        print("Too high!")
                else:
                        print("Too low!")

