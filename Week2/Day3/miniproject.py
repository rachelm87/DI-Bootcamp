#Mini Project Command-Line Tic Tac Toe

#Step 1 - Represent the Game Board!

board = [' '] * 9

#printing board manually
# print(f' {board[0]} | {board[1]} | {board[2]}')
# print('---|---|---')
# print(f' {board[3]} | {board[4]} | {board[5]}')
# print('---|---|---')
# print(f' {board[6]} | {board[7]} | {board[8]}')

#Step 2 - Display the Game Board
#create a function to display current state of board
def display_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]}')

#display_board(board)

#Step 3 - Getting Player Input
# Create a function called player_input(player) to get the player’s move
current_player='X'
# The function should ask the player to enter a position (e.g., row and column numbers).
# #Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
#Think about how to ask the user for input, and how to validate that input.
#ask for their input!
def player_input(player):
    while True:
        position = int(input(f'Player {player}, enter a position between 1 and 9: '))
        number = position - 1
        #check if its valid
        if number <0 or number >8:
            print ("This is an invalid position. Please try again.")
            continue #they need to repeat

        #check if its empty
        if board[number] != ' ':
            print ("This position is already taken. Please try again.")
            continue #they need to repeat it again
    
        board[number] = player
        break

#Step 4 - Checking for a winner
# Create a function called check_win(board, player) to check if the current player has won.
row = [[0,1,2],
       [3,4,5],
       [6,7,8]]
column = [[0,3,6],
          [1,4,7],
          [2,5,8]]

diagonal = [[0,4,8],
            [2,4,6]]

winning_options = row + column + diagonal

def check_win(board, player):
    for options in winning_options: 
        if board[options[0]] == board[options[1]] == board[options[2]] == player:
            return True
    return False

#Step 5 - Checking for a tie
# Create a function to check if the game has resulted in a tie.
# create a function where all the positions are filled in with x's or o's. So basically where everything doesn't equal "-".
def check_for_tie(board):
    if ' ' not in board:
        return True
    return False

#Step #6 - Main Game Loop
#Create a function called play() to manage the game flow.

#initialize the board
def play():
# Initialize the board
    current_player = 'X'

    while True:
        display_board(board)
        player_input(current_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_for_tie(board):
            display_board(board)
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

play()
