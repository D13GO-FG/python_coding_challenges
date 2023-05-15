from src.games import TicTacToe


def test_make_move():
    game = TicTacToe()
    assert game.make_move(1, 1) == True
    assert game.make_move(1, 1) == False


def test_switch_player():
    game = TicTacToe()
    assert game.current_player == "X"
    game.switch_player()
    assert game.current_player == "O"
    game.switch_player()
    assert game.current_player == "X"


def test_get_winner():
    game = TicTacToe()
    game.board = [
        ["X", "O", " "],
        ["O", "X", " "],
        [" ", " ", "X"],
    ]
    assert game.get_winner() == "X"


def test_board_full():
    game = TicTacToe()
    game.board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"],
    ]
    assert game.board_full() == True


def test_game_over():
    game = TicTacToe()
    game.board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"],
    ]
    assert game.game_over() == True


def test_play(capsys):
    game = TicTacToe()
    # Test a tie game
    game.board = [
        ["X", "O", "O"],
        ["O", "X", "X"],
        ["X", "O", "O"],
    ]
    game.play()
    assert "It's a tie!" in capsys.readouterr().out
    # Test X wins
    game = TicTacToe()
    game.board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", " ", "X"],
    ]
    game.play()
    assert "X wins!" in capsys.readouterr().out
    # Test O wins
    game = TicTacToe()
    game.board = [
        ["O", "X", "X"],
        ["O", "O", " "],
        ["O", "X", "X"],
    ]
    game.play()
    assert "O wins!" in capsys.readouterr().out
