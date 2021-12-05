from random import shuffle


def scramble(word):
    """Takes a string parameter named word, and returns a string where the
    first two letters and the last two letters are the same as word, and the
    middle letters of the returned string are the remaining letters from word
    in a random order. A word of length smaller or equal to five letters is
    not changed by the function.

    Args:
        word (String): A string entered to be scrambled.

    Returns:
        word (String): A string that is the input but scrambled.
    """
    if len(word) <= 5:
        return word
    l = []
    for char in word:
        l.append(char)
    middle = l[2:len(word)-2]
    end = l[len(word)-2:]
    shuffle(middle)
    l = l[:2]
    l.append(middle)
    l.append(end)
    word = ""
    print(l)
    for i in range(len(l)):
        for j in range(len(l[i])):
            word = word + str(l[i][j])
    return word
