import os
from src.file_questions import find_phrase_in_file, sum_csv_columns


def test_find_phrasa_in_file():
    # Create a test file and write a phrase in it
    with open("test_file.txt", "w") as f:
        f.write("Hello, world!")

    # Test that the function returns True for the phrase in the file
    assert find_phrase_in_file("Hello", "test_file.txt") == True

    # Test that the function returns False for a phrase not in the file
    assert find_phrase_in_file("Goodbye", "test_file.txt") == False

    # Delete the test file
    os.remove("test_file.txt")


def test_sum_csv_columns():
    # Create a test CSV file
    with open("test_file.csv", "w") as f:
        f.write("1,2,3\n4,5,6\n7,8,9")

    # Test that the function returns the correct sum for each column
    assert sum_csv_columns(0, "test_file.csv") == 12
    assert sum_csv_columns(1, "test_file.csv") == 15
    assert sum_csv_columns(2, "test_file.csv") == 18

    # Delete the test file
    os.remove("test_file.csv")
