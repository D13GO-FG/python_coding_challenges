from src.oo_questions import perfect_squares


def test_perfect_squares():
    # test case 1: N is 30
    assert list(perfect_squares(30)) == [1, 4, 9, 16, 25]

    # test case 2: N is 25
    assert list(perfect_squares(25)) == [1, 4, 9, 16]

    # test case 3: N is 1
    assert list(perfect_squares(1)) == []
