
# Tic Tac Toe Game

## Author
Terran Stone

## Description
This is a graphical Tic Tac Toe game built with Python using the `graphics` library. The game allows two players to play on a 3x3 grid where one player uses "X" and the other uses "O". The game checks for a winner after every move and displays the result once a player wins or if the game ends in a draw.

## Features
- 2-player support
- Graphical user interface (GUI) with a 3x3 grid
- Player 1 uses "X" and Player 2 uses "O"
- Real-time win detection and draw detection
- Interactive clicks to select squares

## Requirements
- Python 3.x
- `graphics.py` library (can be installed by following instructions in the [Graphics Library](https://mcsp.wartburg.edu/zelle/python/))

## How to Run
1. Clone the repository to your local machine.
2. Install the `graphics.py` library if you don't already have it. Instructions for installation are available in the [Graphics Library documentation](https://mcsp.wartburg.edu/zelle/python/).
3. Open the project directory in your terminal.
4. Run the Python program with:
    ```bash
    python tic_tac_toe.py
    ```
5. The game window will appear, and you can play the game by clicking on the squares on the grid.

## Game Instructions
- Player 1 (X) goes first.
- Click on an empty square to place your mark ("X" or "O").
- The game ends when either player wins or all squares are filled (draw).
- A winner is declared if a player gets three marks in a row, column, or diagonal.
- Click anywhere on the window after the game ends to close it.

## Code Structure

### Functions
- **`player_one_x(win, center)`**: Draws an "X" for Player 1.
- **`player_two_circle(win, center)`**: Draws an "O" for Player 2.
- **`square_center(row, col)`**: Calculates the center of each square on the grid.
- **`square_selection(click)`**: Determines which square the player clicked on.
- **`full_not_full(spaces)`**: Checks if all squares have been filled.
- **`winning(spaces)`**: Checks if there is a winner.

### Main Function
- Initializes the game window, creates the grid, and handles player turns.
- Alternates between Player 1 and Player 2 until there is a winner or the game is a draw.

## Example Output
When Player 1 wins:
```
Player 1 wins! Click the window to quit.
```
When Player 2 wins:
```
Player 2 wins! Click the window to quit.
```
If the game is a draw:
```
Game over, it's a draw!
```

## License
This project is open source and available under the MIT License.

## Acknowledgements
- Thanks to John Zelle for the `graphics.py` library.
