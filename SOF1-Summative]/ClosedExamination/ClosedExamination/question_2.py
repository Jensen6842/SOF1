def molecule_to_list(molecule):
    output = []
    temp = ''
    temp2 = ''

    if molecule[0].isupper() is False:
        raise ValueError

    """If the character is uppercase then it is a new molecule. If the
    character is lowercase; if there is no numbers are after uppercase
    then it is the next letter of the molecule, otherwise it is an error.
    If the character is a number then it will be added to the number of the
    molecule. If a new molecule starts and the previous has no number, the
    number is set to 1. Any other character is an error."""
    for i in range(len(molecule)):
        if molecule[i].isupper():
            if temp != '':
                if temp2 == '':
                    temp2 = '1'
                output.append((temp, int(temp2)))
            temp = molecule[i]
            temp2 = ''
        elif molecule[i].islower():
            if temp2 == '':
                temp += molecule[i]
            else:
                raise ValueError
        elif molecule[i].isnumeric():
            temp2 += molecule[i]
        else:
            raise ValueError
    if temp2 == '':
        temp2 = '1'
    output.append((temp, int(temp2)))
    return output
