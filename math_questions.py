def divisible_by_5_not_7(x, y):
    """Function that takes two integers (x and y) and returns a list of numbers between x and y that are divisible by 5 but not by 7"""
    list = []
    for i in range(x, y + 1):
        if i % 5 == 0 and i % 7 != 0:
            list.append(i)
    return list
