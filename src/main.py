import math_questions
import file_questions
import oo_questions
import games


def run():
    while True:
        def printDivider():
            print('-' * 80)

        # display the menu options
        print("\n")
        printDivider()
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
            printDivider()
            print("Find all numbers between x and y that are divisible by 5 but not by 7")
            try:
                x = int(input("Enter x: "))
                y = int(input("Enter y: "))
                print("\n")
                result = math_questions.divisible_by_5_not_7(x, y)
                print(
                    f"The numbers divisible by 5 but not by 7 for number between {x} and {y} are: \n{result}")
                printDivider()
            except:
                print("\n")
                print("It's require input numbers.")
                print('-' * 80)
        elif choice == "2":
            printDivider()
            print("Convert a number to a different base")
            try:
                x = int(input("Enter the number to convert: "))
                b = int(input("Enter the base to convert to: "))
                print("\n")
                result = math_questions.return_value_following_function(x, b)
                print(f"The number {x} in base {b} is equal to {result}.")
                printDivider()
            except:
                print("\n")
                print("It's require input numbers.")
                printDivider()
        elif choice == "3":
            printDivider()
            print("Check if a phrase is in a text file")
            phrase = input("Enter the phrase to search for: ")
            print("\n")
            file_name = "../resources/example.txt"
            result = file_questions.find_phrase_in_file(phrase, file_name)
            if result == True:
                print(f"The phrase '{phrase}' is in the file '{file_name}'")
                printDivider()
            else:
                print(f"The phrase is not in file '{file_name}'")
                printDivider()
        elif choice == "4":
            printDivider()
            print("Sum the entries in a column of a CSV file")
            try:
                column = int(
                    input("Enter the column number to sum (0-indexed): "))
                print("\n")
                file_name = "../resources/example.csv"
                total = file_questions.sum_csv_columns(column, file_name)
                if total != None:
                    print(
                        f"The total sum of column {column} in {file_name} is {total}")
                    printDivider()
            except:
                print("\n")
                print("It's require input numbers.")
                printDivider()
        elif choice == "5":
            printDivider()
            print("Generate all perfect squares less than a number")
            try:
                n = int(input("Enter a number to generate perfect squares up to: "))
                print("\n")
                squares = list(oo_questions.perfect_squares(n))
                print(f"The perfect squares less than {n} are: {squares}")
                printDivider()
            except:
                print("\n")
                print("It's require input numbers.")
                printDivider()
        elif choice == "6":
            printDivider()
            print("Playing Tic Tac Toe")
            print("\n")
            game = games.TicTacToe()
            game.play()
            printDivider()
        elif choice == "0":
            printDivider()
            print("Goodbye!")
            printDivider()
            break
        else:
            printDivider()
            print("Invalid choice, please try again.")
            printDivider()


if __name__ == '__main__':
    run()
