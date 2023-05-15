from src.file_questions import find_phrase_in_file, sum_csv_columns


def test_find_phrasa_in_file():
    actual_result = find_phrase_in_file(
        "Mammography is a critical diagnostic tool for breast cancer, with the ability to detect the disease at its earliest stages.", "/home/ldiego/project-python/cureMetrix_challenge/resources/example.txt")
    print(actual_result)
    assert actual_result == True


def test_sum_csv_columns():
    assert sum_csv_columns(
        0, "/home/ldiego/project-python/cureMetrix_challenge/resources/example.csv") == 15
