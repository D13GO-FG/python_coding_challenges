class TicTacToe:
    def __init__(self) -> None:
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        print("   1  2  3")
        for row in range(3):
            print(row + 1, end=" ")
            for col in range(3):
                print(f"[{self.board[row][col]}]", end="")
            print()

    def get_move(self):
        print("\n")
        print('-' * 28)
        row = int(input(f"{self.current_player}, choose a row (1, 2, 3): "))
        col = int(input(f"{self.current_player}, choose a col (1, 2, 3): "))
        print('-' * 28)
        print("\n")
        return row, col

    def make_move(self, row, col):
        row, col = row - 1, col - 1
        if self.board[row][col] != " ":
            print('-' * 28)
            print("Invalid move, try again")
            print('-' * 28)
            print("\n")
            return False
        self.board[row][col] = self.current_player
        return True

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def get_winner(self):
        # check rows ---
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                return self.board[row][0]
        # check columns |
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]
        # check diagonal \
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        # check diagonal /
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

    def board_full(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    return False
        return True

    def game_over(self):
        return self.get_winner() or self.board_full()

    def play(self):
        while not self.game_over():
            self.print_board()
            row, col = self.get_move()
            flaw = False
            while not flaw:
                flaw = self.make_move(row, col)
                if flaw == True:
                    self.switch_player()
                else:
                    break
            # self.make_move(row, col)
            # self.switch_player()

        self.print_board()
        print("\n")
        print('-' * 28)
        winner = self.get_winner()
        if winner:
            print(f"{winner} wins!")
        else:
            print("It's a tie!")
