def create_chequerboard(n):
    """When given an integer n, returns a string representing a chequerboard
    of size n x n.

    Args:
        n (Integer): Height and width of the chequerboard.

    Returns:
        output (String): A chequerboard drawn using the - and x characters.
        None (Boolean)
    """
    if n < 2:
        return None
    output = ""
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i % 2 == 0:
                first = "x"
                second = "-"
            else:
                first = "-"
                second = "x"
            if j % 2 == 0:
                output = output + first
            else:
                output = output + second
        output = output + "\n"
    return output
