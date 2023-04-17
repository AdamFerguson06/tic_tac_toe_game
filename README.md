# Tic Tac Toe Game

A simple implementation of the classic Tic Tac Toe game using Python and tkinter for the GUI.

## Prerequisites

- Python 3.6 or higher

## Running the Game

1. Clone the repository to your local machine:
```
git clone https://github.com/AdamFerguson06/tic_tac_toe.git
cd tic_tac_toe
```

2. Install tkinter if not already installed:

### For Ubuntu/Debian
````
sudo apt-get install python3-tk
````

### For Fedora
```
sudo dnf install python3-tkinter
```

### For Windows or macOS, tkinter is included in Python 3.1 or later by default

3. Run the frontend code to start the game:

```
python frontend_ui.py
```

A window should open with the Tic Tac Toe game board. Click on the grid cells to make a move. The game will automatically detect a win or a draw and show a message. Click the 'Reset' button to start a new game.

## Components
`tic_tac_toe.py`: Contains the backend code for the game logic, including the TicTacToe class with methods for making moves, checking for a winner, and managing the game state.
`frontend_ui.py`: Contains the frontend code using tkinter for creating the game's GUI and handling user input.
