def perfect_squares(n):
    # initialize the counter variable to 1
    i = 1
    # continue iterating as long as the square of i is less than N
    while i**2 < n:
        # yield the square of i as the next value in the sequence
        yield i**2
        # increment i
        i += 1
