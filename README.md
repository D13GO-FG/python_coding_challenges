# Python Coding Challenges

- [PDF Document with challenges](resources/code-questions-python-pdf.pdf)

---

## Challenges by biotech company:

- [Math Questions](src/math_questions.py)
- [O.O. Questions](src/oo_questions.py)
- [File Questions](src/file_questions.py)
- [Game TicTacToe](src/games.py)

---

# Running!

## Linux and Mac

```bash
git clone https://github.com/D13GO-FG/python_coding_challenges.git
cd python_coding_challenges
python -m venv env
source env/bin/activate
pip install -r requirements.txt
pytest
cd src/
python main.py
```

## Pytest displayed.

```bash
(env) path/python_coding_challenges$ pytest
========================================================================== test session starts ===========================================================================
platform linux -- Python 3.8.10, pytest-7.3.1, pluggy-1.0.0
rootdir: /home/ldiego/project-python/cureMetrix_challenge
collected 12 items

tests/test_file_questions.py ..                                                                                                                                    [ 16%]
tests/test_game.py ......                                                                                                                                          [ 66%]
tests/test_math_questions.py ...                                                                                                                                   [ 91%]
tests/test_oo_questions.py .                                                                                                                                       [100%]

=========================================================================== 12 passed in 0.05s ===========================================================================
```

## Select specific option to run each challenge.

```bash
(env) path/python_coding_challenges/src$ python main.py

--------------------------------------------------------------------------------
Select an option:
1. Find all numbers between x and y that are divisible by 5 but not by 7
2. Convert a number to a different base
3. Check if a phrase is in a text file
4. Sum the entries in a column of a CSV file
5. Generate all perfect squares less than a number
6. Play Tic Tac Toe
0. Quit
--------------------------------------------------------------------------------


> 'your option input'
```

---

## Test Scenarios

| Project Name       | BioTech Company Challenge            |
| ------------------ | ------------------------------------ |
| Client             | \*Confidential\*                     |
| Reference Document | Interview Questions (Python) --> IQP |
| Created By         | Luis Diego Flores                    |
| Creation Date      | 15-05-2023                           |

| Test Scenario ID | Reference | Test Scenario Description                                         | Number of Test Cases |
| ---------------- | --------- | ----------------------------------------------------------------- | -------------------- |
| TS_001           | IQP       | Validate the working of functions of math questions functionality | 3                    |
| TS_002           | IQP       | Validate the working of functions of oo questions functionality   | 1                    |
| TS_003           | IQP       | Validate the working of functions of file questions functionality | 2                    |
| TS_004           | IQP       | Validate the working of game TicTacToe functionality              | 8                    |

---

## TestCases

---

| Test Case ID | Test Scenario                          | Test Case Title                                                                                                                                                   | Pre-requisites                                                | Test Steps                                                                                                                                                                                                      | Test Data      | Expected Result (ER)                                                                                                                                                                                                                         |
| ------------ | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TC_MQ_001    | (TS_001)<br>Math Questions             | Validate function that takes two integers (x and y) and returns a list of numbers between x and y that are divisible by 5 but not by 7                            | 1\. Open console an run: python src/main.py and type option 1 | 1\. Input x value in console<br>2\. Input y value in console<br>3\. Enter                                                                                                                                       | Not Applicable | 1\. If x < y, then view: "The numbers divisible by 5 but not by 7 for number between 2 and 23 are:<br>[numbers list]"<br>2\. If x > y, then view: "The numbers divisible by 5 but not by 7 for number between 2 and 23 are:<br>[empty list]" |
| TC_MQ_002    | (TS_001)<br>Math Questions             | Validate function that takes two integers (x and b) as inputs and returns a string that represents the number x in base b                                         | 1\. Open console an run: python src/main.py and type option 2 | 1\. Input "Enter the number to convert" value in console<br>2\. Input "Enter the base to convert to" value in console<br>3\. Enter                                                                              | Not Applicable | 1\. View:The number N in base B is equal to RESULT.<br>                                                                                                                                                                                      |
| TC_MQ_003    | (TS_001)<br>Math Questions             | Validate function that takes two numbers (x and y) as input and returns the value to the following function (number_to_base).                                     | 1\. Open console an run: python src/main.py and type option 2 | 1\. Input "Enter the number to convert" value in console<br>2\. Input "Enter the base to convert to" value in console<br>3\. Enter                                                                              | Not Applicable | 1\. View:The number N in base B is equal to RESULT.<br>                                                                                                                                                                                      |
| TC_OOQ_001   | (TS_002)<br>OO Questions               | Validate generator (function) that takes a number N and returns all perfect squares less than N.                                                                  | 1\. Open console an run: python src/main.py and type option 5 | 1\. Input "Enter a number to generate perfect squares up to" value in console<br>2\. Enter                                                                                                                      | Not Applicable | 1\. Display: "The perfect squares less than 12 are: [numbers]"<br>                                                                                                                                                                           |
| TC_FQ_001    | (TS_003)<br>File Questions             | Validate function that takes a phrase and a text file as inputs. The function returns True if the phrase is found in the document and returns False otherwise.    | 1\. Open console an run: python src/main.py and type option 3 | 1\. Input "Enter the phrase to search for:" value in console<br>2\. Enter                                                                                                                                       | Not Applicable | 1\. Display: "The phrase {phrase} is in the file {path/file_name}"<br>                                                                                                                                                                       |
| TC_FQ_002    | (TS_003)<br>File Questions             | Validate function that gives a Comma Separated File (csv) and a column number (zero being the left most column) return the sum of all the entries in that column. | 1\. Open console an run: python src/main.py and type option 4 | 1\. Input "Enter the column number to sum (0-indexed):" value in console<br>2\. Enter                                                                                                                           | Not Applicable | 1\. Display: "The total sum of column {n} in {path/file_name} is {final_result}'"<br>                                                                                                                                                        |
| TC_GAME_001  | (TS_004)<br>Game (TicTacToe) Questions | Validate method that run the game once.                                                                                                                           | 1\. Open console an run: python src/main.py and type option 6 | 1\. Input: Playing Tic Tac Toe<br><br><br>1 2 3<br>1 [ ][ ][ ]<br>2 [ ][ ][ ]<br>3 [ ][ ][ ]<br><br><br>\----------------------------<br>X, choose a row (1, 2, 3): {move}<br>X, choose a col (1, 2, 3): {move} | Not Applicable | 1\. Display: "Moves until get winner'"<br>1 2 3<br>1 [X][O][O]<br>2 [X][ ][ ]<br>3 [X][ ][ ]<br><br><br>\----------------------------<br>X wins!                                                                                             |
| TC_GAME_002  | (TS_004)<br>Game (TicTacToe) Questions | Validate method that check the board is printed correctly base en previuos sets.                                                                                  |                                                               |                                                                                                                                                                                                                 | Not Applicable |                                                                                                                                                                                                                                              |
| TC_GAME_003  | (TS_004)<br>Game (TicTacToe) Questions | Validate method that get the moves of the player in console.                                                                                                      |                                                               |                                                                                                                                                                                                                 | Not Applicable |                                                                                                                                                                                                                                              |
| TC_GAME_004  | (TS_004)<br>Game (TicTacToe) Questions | Validate method that make the moves in the board.                                                                                                                 |                                                               |                                                                                                                                                                                                                 | Not Applicable |                                                                                                                                                                                                                                              |
| TC_GAME_005  | (TS_004)<br>Game (TicTacToe) Questions | Validate method that switch the pleayer once the previous player done his move.                                                                                   |                                                               |                                                                                                                                                                                                                 | Not Applicable |                                                                                                                                                                                                                                              |
| TC_GAME_006  | (TS_004)<br>Game (TicTacToe) Questions | Validate method that get the winner of the game.                                                                                                                  |                                                               |                                                                                                                                                                                                                 | Not Applicable |                                                                                                                                                                                                                                              |
| TC_GAME_007  | (TS_004)<br>Game (TicTacToe) Questions | Validate method that check if board is full without winners.                                                                                                      |                                                               |                                                                                                                                                                                                                 | Not Applicable |                                                                                                                                                                                                                                              |
| TC_GAME_008  | (TS_004)<br>Game (TicTacToe) Questions | Validate method that check if the game is over when there is winner or tie.                                                                                       |                                                               |                                                                                                                                                                                                                 | Not Applicable |                                                                                                                                                                                                                                              |

---
