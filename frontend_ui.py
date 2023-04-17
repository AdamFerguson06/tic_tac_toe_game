import tkinter as tk
from tic_tac_toe import TicTacToe

class TicTacToeGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("300x300")
        self.tic_tac_toe = TicTacToe()
        self.create_widgets()

    def create_widgets(self):
        pass

    def on_button_click(self, row, col):
        pass

    def reset_game(self):
        pass

if __name__ == "__main__":
    app = TicTacToeGUI()
    app.mainloop()
