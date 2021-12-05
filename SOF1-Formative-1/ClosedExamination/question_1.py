def create_triangle(n):
    """When given an integer n, returns a string representing a triangle n
    levels high when printed.

    Args:
        n (Integer): Height of the triangle.

    Returns:
        output (String): A triangle drawn using the - and x characters.
        None (Boolean)
    """
    output = ""
    if n >= 0:
        for i in range(1, n+1):
            output = output + "x"*i + "-"*(n-i) + "\n"
        return output
    else:
        return None
        