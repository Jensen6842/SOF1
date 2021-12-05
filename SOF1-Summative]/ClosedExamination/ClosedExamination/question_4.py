def check_level(level):
    # If the level ends with a mine, it isn't feasible.
    if level[-1] == 0:
        return False
    for i in range(len(level)):
        try:
            # If the level is only 1 long, it is feasible if it isn't a 0.
            if len(level) == 1:
                if level[i] == 0:
                    return False
                else:
                    return True
                # If the level starts with a mine it isn't feasible.
            if level[i] == 0:
                return False
            # If the spring's max takes you to a mine, try one less than that.
            elif level[i+level[i]] == 0:
                if level[i] == 1:
                    return False
                else:
                    new_level = level
                    new_level[i] = new_level[i]-1
                    new_level = new_level[i:]
                    if check_level(new_level) is True:
                        return True
                    else:
                        return False
            # If a springs max doesn't take you to a mine, continue.
            else:
                new_level = level[i+level[i]:]
                if check_level(new_level) is True:
                        return True
                else:
                    return False
        # If a spring can jump past the end, it is feasible.
        except IndexError:
            return True
