def text2dictionary(filename):
    airports = {}
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        linesplit = line.split(', ')
        if len(linesplit[2]) > 3:
            linesplit[2] = linesplit[2][:3]
        airports.update({linesplit[1]:[(linesplit[0], linesplit[2])]})
    return airports

print(text2dictionary('data/airport_data.txt'))