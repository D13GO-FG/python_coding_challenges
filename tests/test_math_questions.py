from src.math_questions import divisible_by_5_not_7, number_to_base, return_value_following_function


def test_divisible_by_5_not_7():
    list = [5, 10, 15, 20, 25, 30, 40, 45, 50, 55, 60]
    assert divisible_by_5_not_7(1, 60) == list


def test_number_to_base():
    assert number_to_base(5, 2) == '101'


def test_return_value_following_function():
    assert return_value_following_function(5, 3) == '12'
