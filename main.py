import math_questions
import file_questions


def run():
    print(math_questions.divisible_by_5_not_7(1, 60))
    print(math_questions.number_to_base(5, 3))
    print(math_questions.return_value_following_function(5, 2))
    print(file_questions.find_phrase_in_file(
        "Mammography is a critical diagnostic tool for breast cancer, with the ability to detect the disease at its earliest stages.", "example.txt"))


if __name__ == '__main__':
    run()
