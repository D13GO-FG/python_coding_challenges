from src.math_questions import divisible_by_5_not_7, number_to_base, return_value_following_function


def test_divisible_by_5_not_7():
    # validate that return a list with the numbers divisible by 5 not 7
    assert divisible_by_5_not_7(
        1, 60) == [5, 10, 15, 20, 25, 30, 40, 45, 50, 55, 60]
    # validate that return empty list because of range 21 to 24 there're not number divisible by 5 not 7
    assert divisible_by_5_not_7(21, 24) == []


def test_number_to_base():
    # validate return number in base 2
    assert number_to_base(5, 2) == '101'
    # validate return number in base 10
    assert number_to_base(100, 10) == "100"
    # validate return number in base 100
    assert number_to_base(5000, 100) == "500"


def test_return_value_following_function():
    # validate return number in base 3
    assert return_value_following_function(5, 3) == '12'
    # validate return number in base 10
    assert return_value_following_function(100, 10) == "100"
    # validate return number in base 100
    assert return_value_following_function(4000, 100) == "400"
