import csv


def find_phrase_in_file(phrase, file_name):
    """Function that takes a phrase and a text file as inputs. The function returns True if the phrase is found in the document and returns False otherwise."""

    # open the file specified in read mode by default.
    with open(file_name) as file:
        # checking if the given phrase is in any line of the file, return True.
        for line in file:
            if phrase in line:
                return True
    # doesn't find the phrase, then return False.
    return False


def sum_csv_columns(column, file_name):
    """Give a Comma Separated File (csv) and a column number (zero being the left most column) return the sum of all the entries in that column"""

    # track the sum by columns.
    total = 0
    # open the file csv specified in read mode by default.
    with open(file_name) as file:
        # create a CSV reader object using the file.
        reader = csv.reader(file)
        # iterates through each row.
        for row in reader:
            # add the value of the row in correct column.
            total += int(row[column])
    # return total sum of the entries in the specified column.
    return total
