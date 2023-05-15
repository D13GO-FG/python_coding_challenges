from src.oo_questions import perfect_squares


def test_perfect_squares():
    list = []
    # iterate over the values produced by the "perfect_squares" generator with a maximum value of 30
    for square in perfect_squares(30):
        # print each perfect square value
        list.append(square)
    assert list == [1, 4, 9, 16, 25]
