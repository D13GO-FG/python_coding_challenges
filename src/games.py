class TicTacToe:
    def __init__(self) -> None:
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    # method that check the board is printed correctly base en previuos sets.

    def print_board(self):
        print("   1  2  3")
        for row in range(3):
            print(row + 1, end=" ")
            for col in range(3):
                print(f"[{self.board[row][col]}]", end="")
            print()

    # method that get the moves of the player in console

    def get_move(self):
        print("\n")
        print('-' * 28)
        row = int(input(f"{self.current_player}, choose a row (1, 2, 3): "))
        col = int(input(f"{self.current_player}, choose a col (1, 2, 3): "))
        print('-' * 28)
        print("\n")
        return row, col

    # method that make the moves in the board

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

    # method that switch the pleayer once the previous player done his move

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    # method that get the winner of the game

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

    # method that check if board is full without winners

    def board_full(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    return False
        return True

    # method that check if the game is over when there is winner or tie

    def game_over(self):
        return self.get_winner() or self.board_full()

    # method that run the game once.

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
