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
