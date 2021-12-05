sample_text = (" As Python s creator, I'd like to say a few words about its "+
              "origins adding a bit of personal philosophy. "+
              "Over six years ago in December I was looking for a "+
              "hobby programming project that would keep me occupied "+
              "during the week around Christmas. My office, "+
              "a government run research lab in Amsterdam would be closed "+
              "but I had a home computer and not much else on my hands "+
              " I decided to write an interpreter for the new scripting "+
              "language  I had been thinking about lately a descendant of ABC "+
              "that would appeal to UnixC hackers I chose Python as a "+
              "working title for   the project being in a slightly irreverent "+
              "mood and a big fan of Monty Python s Flying Circus.  ")

import string

######################### EXERCISE 1 ##########################################

def split_text(text, separators):    
    output = []
    temp = ""
    for char in text:
        if char not in separators:
            temp += char
        elif temp:
            output.append(temp)
            temp = ""
    if temp:
        output.append(temp)
    return output

######################### EXERCISE 2 ##########################################

def get_words_frequencies(text):
    output = {}
    text_list = split_text(text, string.punctuation + " ")
    print(text_list)
    for word in text_list:
        word = word.lower()
        if word in output:
            output[word] = output[word] + 1
        else:
            output[word] = 1
    return output
print(get_words_frequencies(sample_text))

######################### EXERCISE 3 ##########################################

def flatten(list_2D):
    list_1D = []
    for i in range(len(list_2D)):
        for j in range(len(list_2D[i])):
            list_1D.append(list_2D[i][j])
    return list_1D

######################### EXERCISE 4 ##########################################

def rasterise(list_1D, width):
    output = []
    if width < 1 or len(list_1D) % width != 0:
        return None
    else:
        for row in range(int(len(list_1D)/width)):
            output.append(list_1D[row*width:(row+1)*width])
        return output