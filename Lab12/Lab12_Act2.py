# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 12-2
# Date:         12 06 2021
#

from random import *
import turtle


def count_down(count):
    if count == 0:
        print('Pig!')
    else:
        print(count)
        count_down(count - 1)


print("Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to hold:")
print("If the player rolls a 1, they score nothing and it becomes the next player's turn.")
print("If the player rolls any other number, it is added to their turn total and the player's turn continues.")
print("If a player chooses to hold, their turn total is added to their score, and it becomes the next player's turn.")
amount_won = 0
points = 0
player_number = 1
total1 = 0
total2 = 0
player1_points = open('player1.txt', 'w')
player2_points = open('player2.txt', 'w')
count_down(3)


def peppa():
    turtle.pensize(4)
    turtle.hideturtle()
    turtle.colormode(255)
    turtle.color((255, 155, 192), "pink")
    turtle.setup(840, 500)
    turtle.speed(20)
    # Nose
    turtle.pu()
    turtle.goto(-100, 100)
    turtle.pd()
    turtle.seth(-30)
    turtle.begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            turtle.lt(3)  # turn left 3 degrees
            turtle.fd(a)  # The step length of a forward
        else:
            a = a - 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.end_fill()
    turtle.pu()
    turtle.seth(90)
    turtle.fd(25)
    turtle.seth(0)
    turtle.fd(10)
    turtle.pd()
    turtle.pencolor(255, 155, 192)
    turtle.seth(10)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.color(160, 82, 45)
    turtle.end_fill()
    turtle.pu()
    turtle.seth(0)
    turtle.fd(20)
    turtle.pd()
    turtle.pencolor(255, 155, 192)
    turtle.seth(10)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.color(160, 82, 45)
    turtle.end_fill()
    # Head
    turtle.color((255, 155, 192), "pink")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(41)
    turtle.seth(0)
    turtle.fd(0)
    turtle.pd()
    turtle.begin_fill()
    turtle.seth(180)
    turtle.circle(300, -30)
    turtle.circle(100, -60)
    turtle.circle(80, -100)
    turtle.circle(150, -20)
    turtle.circle(60, -95)
    turtle.seth(161)
    turtle.circle(-300, 15)
    turtle.pu()
    turtle.goto(-100, 100)
    turtle.pd()
    turtle.seth(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            turtle.lt(3)  # turn left 3 degrees
            turtle.fd(a)  # The step length of a forward
        else:
            a = a - 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.end_fill()
    # Ears
    turtle.color((255, 155, 192), "pink")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-7)
    turtle.seth(0)
    turtle.fd(70)
    turtle.pd()
    turtle.begin_fill()
    turtle.seth(100)
    turtle.circle(-50, 50)
    turtle.circle(-10, 120)
    turtle.circle(-50, 54)
    turtle.end_fill()
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-12)
    turtle.seth(0)
    turtle.fd(30)
    turtle.pd()
    turtle.begin_fill()
    turtle.seth(100)
    turtle.circle(-50, 50)
    turtle.circle(-10, 120)
    turtle.circle(-50, 56)
    turtle.end_fill()
    # Eyes
    turtle.color((255, 155, 192), "white")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-20)
    turtle.seth(0)
    turtle.fd(-95)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.color("black")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(12)
    turtle.seth(0)
    turtle.fd(-3)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    turtle.color((255, 155, 192), "white")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-25)
    turtle.seth(0)
    turtle.fd(40)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.color("black")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(12)
    turtle.seth(0)
    turtle.fd(-3)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    # Gill
    turtle.color((255, 155, 192))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-95)
    turtle.seth(0)
    turtle.fd(65)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    # mouth
    turtle.color(239, 69, 19)
    turtle.pu()
    turtle.seth(90)
    turtle.fd(15)
    turtle.seth(0)
    turtle.fd(-100)
    turtle.pd()
    turtle.seth(-80)
    turtle.circle(30, 40)
    turtle.circle(40, 80)
    turtle.exitonclick()
    return


def rolling_outcome():  # will provide a random number on the die
    '''the rolling outcome function is essentially the die. it
    provides a random integer from 1,6 and returns it
    '''
    number = randint(1, 6)
    return number


def holding_outcome(points):  # while find the amount of points won by a player in a round
    '''holding outcome takes the results from your turn and finds
    the points you won that round and returns it
    '''
    amount_won = 0
    amount_won += points
    return amount_won


def gameturn():  # 1 round in a game
    '''the game turn function is the largest function in the game
    and involves the most code. the code first asks for rolling or holding
    and then depending on your answer, it calls rolling_outcome or holding_outcome
    the code is basically what happens in a single turn.
    '''
    global points
    global total1
    global total2

    number = rolling_outcome()
    while number != 1:
        global player_number
        player_choice = input('roll or hold? ')  # makes decision

        if player_choice == 'roll':
            number = (rolling_outcome())  # rolls dice
            points += number  # gives points based on number
            print('you rolled a', number)

        if player_choice == 'hold':  # saves points for player
            amount_won = holding_outcome(points)  # adds up points

            if player_number == 1:  # decides which player gets the points
                player1_points.write(str(amount_won))  # writes the points collected to a string
                total1 += amount_won  # adds points to total
                player_number += 1  # trasfers whos turn it is
                print('player 1 has', total1, 'points')
                if total1 >= 100:
                    print('player 1 wins')
                    break
                print("it is now player 2's turn")

            else:
                player_number == 2  # decides which player gets the points
                player2_points.write(str(amount_won))  # writes the points collected to a string
                total2 += amount_won  # adds points to total
                player_number -= 1  # changes turns
                print('player 2 has', total2, 'points')
                if total2 >= 100:
                    print('player 2 wins')
                    break
                print("it is now player 1's turn")

            break

        if number == 1:  # ends your turn and you get no points
            print("zero points rewarded")
            print("enter hold to start other player's turn")
            try:
                print('enter hold 2 times. 1 for each of two prompts')
                player_choice = input('roll or hold? ')
                if player_choice == 'roll':
                    value = 1 / 0
                    print(value)
            except:
                print('please enter "hold" 2 times')
                player_choice = input('roll or hold? ')

            amount_won = 0
            total1 += 0
            total2 += 0
            break


while total1 < 100 and total2 < 100:  # lets the game continue until someone wins
    gameturn()  # rounds
    points = 0  # resets the points so extra points aren't given
    amount_won = 0  # resets this as well

screen = turtle.Screen()
screen.bgcolor('lightblue')
pen = turtle.Turtle()
pen.penup()
pen.goto(-300, 20)
pen.write('Player 1', align='left', font=("Arial", 20, "bold"))
pen.goto(300, 20)
pen.write('Player 2', align='right', font=("Arial", 20, "bold"))
pen.goto(0, 100)
pen.write('Pig', align='center', font=("Arial", 100, "bold"))
pen.goto(-300, 0)
pen.write('total points: {}'.format(total1), align='left', font=("Arial", 10, "bold"))
pen.goto(300, 0)
pen.write('total points: {}'.format(total2), align='right', font=("Arial", 10, "bold"))
pen.goto(0, -150)
pen.write("WINNER!", align='center', font=("Arial", 100, "bold"))
peppa()
turtle.done()
player1_points.close()
player2_points.close()
