from random import randint

# The board for holding ship locations
HIDDEN_BOARD = [[" "] * 9 for x in range(9)]
# The board that shows hits and misses
GUESS_BOARD = [[" "] * 9 for i in range(9)]

def print_board(board):
    print("  A B C D E F G H I")
    print("  +---------------+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8
}
# The computer creates random ships 
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,9), randint(0,9)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

# The player selects a row and a column
def get_ship_location():
    row = input("Enter the row of the ship: ")
    while row not in "123456789":
        print('Please select a valid row')
        row = input("Enter the row of the ship: ")
    column = input("Enter the column of the ship: ")
    while column not in "ABCDEFGHI":
        print('Please select a valid column')
        column = input("Enter the column of the ship: ")
    return int(row) - 1, letters_to_numbers[column]

# Checking if all the ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

#  Turn count, notify player if hit or miss
if __name__ == "__main__":
    create_ships(HIDDEN_BOARD)
    turns = 15
    while turns > 0:
        print('Guess a location')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("You already guessed that")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("Miss")
            GUESS_BOARD[row][column] = "-"   
            turns -= 1     
        if count_hit_ships(GUESS_BOARD) == 5:
            print("Congratulations, You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")