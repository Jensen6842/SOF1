def encrypt(message, shifts, alphabet):
    """Given a plain text message T of n characters using alphabet A of m
    letters, and a list of n positive integers from the set {0,2,...,k-1}, T
    is encrypted by shifted the k^th character T[k] by an amount S[k].

    Args:
        message (string): The plain text message.
        shifts (list): A list of positive integers to shift the plain text.
        alphabet (string): The alphabet used in the shift.

    Raises:
        ValueError: The number of values in shift is not equal to the number
                    of letters in the plain text message.
        ValueError: A value in the shift is either negative, or greater than
                    or equal to the length of the alphabet.
        ValueError: A character in the message is not in the alphabet.

    Returns:
        string: The cipher text message.
    """
    MESSAGE_LEN = len(message)
    ALPHABET_LEN = len(alphabet)

    if len(shifts) != MESSAGE_LEN:
        raise ValueError
    for i in shifts:
        if (i <= 0) or (i >= ALPHABET_LEN):
            raise ValueError

    cipher = ''
    for i in range(MESSAGE_LEN):
        if message[i] not in alphabet:
            raise ValueError
        # Finds the value of the character in alphabet and applies the shift.
        # Mod added to make sure alphabet loops back to the start of itself.
        value = alphabet.find(message[i])
        new_value = (value+shifts[i]) % ALPHABET_LEN
        cipher = cipher + alphabet[new_value]

    return cipher
