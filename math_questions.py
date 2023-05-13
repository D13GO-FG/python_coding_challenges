def divisible_by_5_not_7(x, y):
    """Function that takes two integers (x and y) and returns a list of numbers between x and y that are divisible by 5 but not by 7"""
    list = []
    for i in range(x, y + 1):
        # checks whether it is divisible by 5 but not divisible by 7, validaing if remainder is equal to zero is divisible.
        if i % 5 == 0 and i % 7 != 0:
            list.append(i)
    return list


def number_to_base(x, b):
    """Function that takes two integers (x and b) as inputs and returns a string that represents the number x in base b"""
    if x == 0:
        return "0"
    list = []
    while x:
        # appends the remainder of x divided by b to the list.
        list.append(str(int(x % b)))
        # updates the value of x to be the floor division of x by b.
        x //= b
    # concatenating the elements in list in reverse order.
    return "".join(list[::-1])


def return_value_following_function(x, y):
    """Function that takes two numbers (x and y) as input and returns the value to the following function."""
    return number_to_base(x, y)
