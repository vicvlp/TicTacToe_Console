"""
Tic-Tac-Toe Console Game

A two-player command-line implementation of the classic Tic-Tac-Toe game.

Features:
- Chess-style board coordinates (a1, b2, c3, etc.)
- Player name input
- Win/draw detection
- In-game commands for flexibility
- Replay functionality

Game Commands:
- Enter cell coordinates (e.g., 'a1', 'b2') to make a move
- 'stop' - quit the current game session
- 'next' - restart game with same players (abandon current game)
- 'new' - restart with new players

Usage:
    python TicTacToe_Console.py

Author: Viktor Pichugin
Email: vicvlp@mail.ru | vicgm4ay@gmail.ru
Date: 2025.10.20
Version: 1.0
"""

def start_init_game():  # Initial game setup
    # Initializes the game, requests player names and returns them
    print("Welcome to Tic-Tac-Toe!")
    player1 = input("Player 1, enter your name: ").strip()
    player2 = input("Player 2, enter your name: ").strip()
    return player1, player2

def create_board():  # Create game board
    # Creates and returns an empty 3x3 game board in chess notation format
    return {
        'a1': '-', 'b1': '-', 'c1': '-',
        'a2': '-', 'b2': '-', 'c2': '-',
        'a3': '-', 'b3': '-', 'c3': '-'
    }

def print_board(board):  # Display game board
    # Prints the current game board state to console in chess notation format
    print("\n   a b c")  # Header with column letters
    print(f"1  {board['a1']} {board['b1']} {board['c1']}")  # Row 1
    print(f"2  {board['a2']} {board['b2']} {board['c2']}")  # Row 2
    print(f"3  {board['a3']} {board['b3']} {board['c3']}\n")  # Row 3

def get_available_moves(board):  # Available cells for move
    # Returns list of available cells for move. Filtered by content
    return [key for key, value in board.items() if value == '-']

def make_move(board, move, symbol):  # Make a move
    # Updates the board and returns new state after move
    board[move] = symbol
    return board

def check_win(board, symbol):  # Check for win
    # Checks if there's a winning combination for specified symbol X or O
    # All possible winning lines in chess notation format
    lines = [
        # Horizontal lines (rows)
        ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
        # Vertical lines (columns)
        ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
        # Diagonals
        ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']
    ]
    for line in lines:
        if all(board[cell] == symbol for cell in line):
            return True
    return False

def check_draw(board):  # Check for draw
    # Checks if draw has occurred (all cells are filled)
    return '-' not in board.values()

def game_loop(player1, player2):  # Main game loop
    board = create_board()  # Create game board with initial values
    current_player = (player1, 'X')  # First player starts with X
    game_active = True  # Current game status (True - on, False - off)

    while game_active:
        print_board(board)  # Display current game board
        cur_player_name, sym = current_player  # Current player name and symbol they're using ('X', 'O')
        available_moves = get_available_moves(board)  # Cells available for move

        print('Help \nAvailable commands:')
        print('"stop" - end the game')
        print('"next" - play again')
        print('"new" - new game with new players\n')
        print(f'Available cells for move: {available_moves}\n')
        move = input(f'{cur_player_name}, enter cell for {sym}: ').strip().lower()

        if move == 'stop':  # End game early
            print('\nGame stopped')
            return  
          
        if move == 'next':  # Start new game with same players
            print('\nNew game with same players')
            print(f"Current players: 1. {player1};  2. {player2}\n")
            board = create_board()  # Create game board with initial values
            current_player = (player1, 'X')  # First player starts with X
            game_active = True  # Current game status (True - on, False - off)
            continue
          
        if move == 'new':  # Start new game with new players
            print('\nNew game with new players')
            player1, player2 = start_init_game()
            board = create_board()  # Create game board with initial values
            current_player = (player1, 'X')  # First player starts with X
            continue

        if move not in available_moves:  # If move is invalid - cell is occupied or doesn't exist
            print('\nError! Invalid move. Please try again')
            continue

        # Execute move
        board = make_move(board, move, sym)

        # Check for win
        if check_win(board, sym):
            print_board(board)  # Final board display
            print(f'{cur_player_name} won. Congratulations!\n')
            game_active = False
        # Check for draw
        elif check_draw(board):
            print_board(board)  # Final board display
            print('Game ended in a draw\n')
            game_active = False
        else:
            # Pass turn to other player
            current_player = (player2, 'O') if current_player[0] == player1 else (player1, 'X')

        # Offer to play again
        if game_active == False:
          replay = input('Want to play again? (Y - yes; any other - no): ').strip().upper()
    
          if replay == 'Y':  # Start new game with same players
              print('\nNew game with same players')
              print(f"Current players: 1. {player1};  2. {player2}\n")
              board = create_board()  # Create game board with initial values
              current_player = (player1, 'X')  # First player starts with X
              game_active = True  # Current game status (True - on, False - off)
              continue
            
          else:
              print('\nGame finished')
              print('Thank you for playing!')
              break

# Program start
if __name__ == "__main__":
    players = start_init_game()
    game_loop(*players)