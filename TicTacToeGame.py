# tic_tac_toe.py

# Initialize the game board
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

# Function to display the current board
def display_board():
    for row in board:
        print(' '.join(row))

# Test the display_board function
display_board()


# Function to handle player input
def get_player_move():
    while True:
        try:
            row = int(input("Enter row number (1-3): ")) - 1
            col = int(input("Enter column number (1-3): ")) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '-':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Test the get_player_move function
row, col = get_player_move()
print("Player move:", row, col)



# Function to check for a winner
def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return board[0][2]
    
    # Check for a draw
    if all(board[i][j] != '-' for i in range(3) for j in range(3)):
        return 'Draw'
    
    # No winner yet
    return None

# Test the check_winner function
board = [
    ['X', '-', 'O'],
    ['-', 'X', 'O'],
    ['-', '-', 'X']
]
print("Winner:", check_winner())
# Main game loop
def main():
    current_player = 'X'
    while True:
        display_board()
        print("Player", current_player + "'s turn")
        row, col = get_player_move()
        board[row][col] = current_player
        winner = check_winner()
        if winner:
            display_board()
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print("Player", winner, "wins!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    main()


