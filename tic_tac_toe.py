class TicTacToe:

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while not self.check_winner() and not self.is_full():
            self.display_board()
            row, col = map(int, input(f"Player {self.current_player}'s turn. Enter row and column (0-2) separated by space: ").split())
            if self.make_move(row, col):
                if self.check_winner():
                    self.display_board()
                    print(f"Player {self.current_player} wins!")
                elif self.is_full():
                    self.display_board()
                    print("It's a draw!")
                else:
                    self.switch_player()
            else:
                print("Invalid move, try again.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
