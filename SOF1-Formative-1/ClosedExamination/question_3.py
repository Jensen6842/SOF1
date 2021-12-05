def sum_integers(start, end):
    """Takes two positive integers, start and end, and returns the sum of all
    integers comprised between start and end inclusive.

    Args:
        start (Integer): The first value in the sum.
        end (Integer): The final value in the sum.

    Returns:
        output [Integer]: The sum of all integers comprised between start and
        end inclusive.
        -1 [Integer] : Returned if the values of start or end are below 0 or
        if the value of end is below the value of start.
    """
    if start < 0 or end < 0 or end < start:
        return -1
    output = 0
    for i in range(start, end+1):
        output += i
    return output
