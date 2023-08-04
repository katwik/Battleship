from random import randint

Hidden_Board=[[' ']*9 for x in range(9)]
Guess_Board=[[' ']*9 for x in range(9)]

letters_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8}

def print_board(board):
    print("  A B C D E F G H I")
    print(" +-----------------+")
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

def get_ship_location():
    row=input('Please enter a ship row 1-9 ')
    while row not in '123456789':
        print("Please enter a valid row ")
        row=input('Please enter a ship row 1-9 ')
    column=input('Please enter a ship column A-I ')
    while column not in 'ABCDEFGHI':
        print("Please enter a valid column ")
        column=input('Please enter a ship column A-I ')
    return int(row)-1,letters_to_num[column]

#Function that creates the ships
def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='X':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = 'X'



def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X':
                count+=1
    return count

create_ships(Hidden_Board)
turns = 15
while turns > 0:
    print('Welcome to Battleship!')
    print_board(Guess_Board)
    row,column =get_ship_location()
    if Guess_Board[row][column] == '-':
        print(' You already guessed that ')
    elif Hidden_Board[row][column] =='X':
        print(' Congratulations, you made a hit! ')
        Guess_Board[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry, You missed')
        Guess_Board[row][column] = '-'
        turns -= 1
    if  count_hit_ships(Guess_Board) == 5:
        print("Congratulations you have sunk all the battleships ")
        break
    print(' You have ' +str(turns) + ' turns remaining ')
    if turns == 0:
        print('Game Over ')
        