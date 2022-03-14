# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 7a_1
# Date:         10 18 2021
#



#create board as 2d list
board = [['.','O','.','O','.','O','.','O'],
         ['O','.','O','.','O','.','O','.'],
         ['.','O','.','O','.','O','.','O'],
         ['.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.'],
         ['o','.','o','.','o','.','o','.'],
         ['.','o','.','o','.','o','.','o'],
         ['o','.','o','.','o','.','o','.']]

# loop through list to print the board to the screen for the game
while True:
    print('board')
    #for loop to traverse through each column
    for i in range(0, 8):
        #for loop for each row
        for j in range(0, 8):
            print(board[i][j], end=" ")
        print("")

# ask user to input values for start and finish place of the piece
    row = int(input('Row: '))
    column = int(input('Column: '))

#if check pieces at location
    if board[row][column]=='.':
        print("Error: No piece at the location")
        # ends the loop
        break
#else to trasnfer pieces
    else:
        #grabs location and assigns to piece
        piece=board[row][column]
        #replcaes location with blank space
        board[row][column]='.'

        #ask user for transfer location
        print("Enter location at which piece is to be transferred")

        #user inputs for transfer
        row=int(input("Row: "))
        column=int(input("Column: "))
        #re-assign piece to new location
        board[row][column]=piece
