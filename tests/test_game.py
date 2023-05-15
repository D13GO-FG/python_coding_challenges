from src.games import TicTacToe


def test_make_move():
    game = TicTacToe()
    # fill on space first time
    assert game.make_move(1, 1) == True
    # space already fulled on
    assert game.make_move(1, 1) == False


def test_switch_player():
    game = TicTacToe()
    # validate if the turn is for player X
    assert game.current_player == "X"
    game.switch_player()
    # validate if switch player works, now player is O
    assert game.current_player == "O"
    # validate if switch player again works, now player is X
    game.switch_player()
    assert game.current_player == "X"


def test_get_winner():
    game = TicTacToe()
    game.board = [
        ["X", "O", " "],
        ["O", "X", " "],
        [" ", " ", "X"],
    ]
    # validate diagonal \
    assert game.get_winner() == "X"

    game = TicTacToe()
    game.board = [
        ["X", "X", "O"],
        ["O", "O", " "],
        ["O", "X", " "],
    ]
    # validate diagonal /
    assert game.get_winner() == "O"

    game = TicTacToe()
    game.board = [
        ["X", "X", "O"],
        ["X", "O", "O"],
        ["X", " ", " "],
    ]
    # validate columns |
    assert game.get_winner() == "X"

    game = TicTacToe()
    game.board = [
        ["X", "X", "O"],
        ["O", "O", "O"],
        ["X", " ", " "],
    ]
    # validate rows ---
    assert game.get_winner() == "O"


def test_board_full():
    game = TicTacToe()
    game.board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"],
    ]
    # validate board full without winner
    assert game.board_full() == True


def test_game_over():
    game = TicTacToe()
    game.board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"],
    ]
    # validate winner or board full with winner
    assert game.game_over() == True


def test_play(capsys):
    game = TicTacToe()
    game.board = [
        ["X", "O", "O"],
        ["O", "X", "X"],
        ["X", "O", "O"],
    ]
    game.play()
    # validate a tie game
    assert "It's a tie!" in capsys.readouterr().out

    game = TicTacToe()
    game.board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", " ", "X"],
    ]
    game.play()
    # validate player X wins
    assert "X wins!" in capsys.readouterr().out

    game = TicTacToe()
    game.board = [
        ["O", "X", "X"],
        ["O", "O", " "],
        ["O", "X", "X"],
    ]
    game.play()
    # validate player O wins
    assert "O wins!" in capsys.readouterr().out
