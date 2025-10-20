# Tic-Tac-Toe Console Game

A Python implementation of the classic Tic-Tac-Toe game for two players in the command line.

## Features

*   **Intuitive Interface:** Game board displayed in chess notation format (columns a-c, rows 1-3)
*   **Player Names:** Custom player names at startup
*   **Smart Game Detection:** Automatic win and draw detection
*   **Flexible Commands:** Special in-game commands for better control:
    *   `stop` - immediately end the game session
    *   `next` - start new game with same players (abandons current game)
    *   `new` - start new game with new players
*   **Replay System:** Play multiple games without restarting the program

## How to Play

1.  Run the script: `python TicTacToe_Console.py`
2.  Enter player names when prompted
3.  Players take turns entering cell coordinates (e.g., `a1`, `b2`, `c3`) to place their symbol (`X` or `O`)
4.  Game continues until a player wins or the game ends in a draw

## In-Game Commands

- **Move:** Enter cell coordinates (a1, b2, c3, etc.)
- **`stop`:** Completely ends the gaming session
- **`next`:** Immediately starts a new game with the same players (current game is abandoned)
- **`new`:** Starts a new game with new player names

## Requirements

*   Python 3.x

## Installation & Running

```bash
# Clone or download the repository
git clone <[repository-url](https://github.com/vicvlp/TicTacToe_Console.git)>

# Navigate to the directory
cd TicTacToe

# Run the game
python TicTacToe_Console.py
