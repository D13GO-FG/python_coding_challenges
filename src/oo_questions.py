def perfect_squares(n):
    """Generator that takes a number N and returns all perfect squares less than N."""
    # initialize the counter variable to 1
    i = 1
    # continue iterating as long as the square of i is less than N
    while i**2 < n:
        # yield the square of i as the next value in the sequence
        yield i**2
        # increment i
        i += 1
