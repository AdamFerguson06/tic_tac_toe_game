import tkinter as tk
from tkinter import messagebox
from tic_tac_toe import TicTacToe

class TicTacToeGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("400x250")
        self.tic_tac_toe = TicTacToe()
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self, text=' ', width=10, height=3,
                                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                self.buttons[row][col].grid(row=row, column=col)

        self.reset_button = tk.Button(self, text='Reset', command=self.reset_game)
        self.reset_button.grid(row=3, columnspan=3)

    def on_button_click(self, row, col):
        if self.tic_tac_toe.make_move(row, col):
            self.buttons[row][col].config(text=self.tic_tac_toe.current_player)
            if self.tic_tac_toe.check_winner():
                self.display_result(f"Player {self.tic_tac_toe.current_player} wins!")
            elif self.tic_tac_toe.is_full():
                self.display_result("It's a draw!")
            else:
                self.tic_tac_toe.switch_player()
        else:
            tk.messagebox.showerror("Invalid move", "Cell is already occupied, choose another one.")

    def display_result(self, message):
        tk.messagebox.showinfo("Game Over", message)
        self.reset_game()

    def reset_game(self):
        self.tic_tac_toe = TicTacToe()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ')

if __name__ == "__main__":
    app = TicTacToeGUI()
    app.mainloop()
