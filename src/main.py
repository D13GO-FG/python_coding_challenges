import math_questions
import file_questions
import oo_questions
import games


def run():
    while True:
        # display the menu options
        print("\n")
        print('-' * 80)
        print("Select an option:")
        print("1. Find all numbers between x and y that are divisible by 5 but not by 7")
        print("2. Convert a number to a different base")
        print("3. Check if a phrase is in a text file")
        print("4. Sum the entries in a column of a CSV file")
        print("5. Generate all perfect squares less than a number")
        print("6. Play Tic Tac Toe")
        print("0. Quit")
        print('-' * 80)
        print("\n")

        # get the user's choice
        choice = input("> ")

        # perform the corresponding action based on the user's choice
        if choice == "1":
            print('-' * 80)
            print("Find all numbers between x and y that are divisible by 5 but not by 7")
            try:
                x = int(input("Enter x: "))
                y = int(input("Enter y: "))
                result = math_questions.divisible_by_5_not_7(x, y)
                print(result)
                print('-' * 80)
            except:
                print("It's require input numbers.")
                print('-' * 80)
        elif choice == "2":
            print('-' * 80)
            print("Convert a number to a different base")
            try:
                x = int(input("Enter the number to convert: "))
                b = int(input("Enter the base to convert to: "))
                result = math_questions.return_value_following_function(x, b)
                print(result)
                print('-' * 80)
            except:
                print("It's require input numbers.")
                print('-' * 80)
        elif choice == "3":
            print('-' * 80)
            print("Check if a phrase is in a text file")
            phrase = input("Enter the phrase to search for: ")
            file_name = "../resources/example.txt"
            result = file_questions.find_phrase_in_file(phrase, file_name)
            if result == True:
                print(f"The phrase '{phrase}' is in the file '{file_name}'")
                print('-' * 80)
            else:
                print(f"The phrase is not in file '{file_name}'")
                print('-' * 80)
        elif choice == "4":
            print('-' * 80)
            print("Sum the entries in a column of a CSV file")
            try:
                column = int(
                    input("Enter the column number to sum (0-indexed): "))
                file_name = "../resources/example.csv"
                total = file_questions.sum_csv_columns(column, file_name)
                print(
                    f"The total sum of column {column} in {file_name} is {total}")
                print('-' * 80)
            except:
                print("It's require input numbers.")
                print('-' * 80)
        elif choice == "5":
            print('-' * 80)
            print("Generate all perfect squares less than a number")
            try:
                n = int(input("Enter a number to generate perfect squares up to: "))
                squares = list(oo_questions.perfect_squares(n))
                print(f"The perfect squares less than {n} are: {squares}")
            except:
                print("It's require input numbers.")
        elif choice == "6":
            print('-' * 80)
            print("Playing Tic Tac Toe")
            game = games.TicTacToe()
            game.play()
            print('-' * 80)
        elif choice == "0":
            print('-' * 80)
            print("Goodbye!")
            print('-' * 80)
            break
        else:
            print('-' * 80)
            print("Invalid choice, please try again.")
            print('-' * 80)


if __name__ == '__main__':
    run()
