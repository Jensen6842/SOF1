#Exercise 0

months = {'1':'january','2':'february','3':'march','4':'april','5':'may','6':'june','7':'july','8':'august','9':'september','10':'october','11':'november','12':'december'}
numbers = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
periodic = {'H':'Hydrogen','He':'Helium','Li':'Lithium','Be':'Berilium','B':'Boron','C':'Carbon','N':'Nitrogen'}
roman = {}
roman.update({100000:'T',1000:'M',500:'D',100:'K',50:'L',10:'X',5:'X',1:'I'})
roman[100] = 'C'

#Exercise 1

def display_dico(dico):
    for key, val in dico.items():
        print(key, "-->", val)

#Exercise 2

def concat_dico(dico1, dico2):
    dico3 = {}
    dico3.update(dico1)
    dico3.update(dico2)
    for key1 in dico1:
        for key2 in dico2:
            if key1 == key2:
                dico3[key1] = [dico1[key1], dico2[key1]]
    return(dico3)

#Exercise 3

def map_list(keys, values):
    dico = {}
    for i in range(len(keys)):
        if keys[i] in dico:
            print("Error, keys list has duplicates.")
            return None
        else:
            dico.update({keys[i]:values[i]})
    return dico

#Exercise 4

def reverse_dictionary(dico):
    rdico = {}
    for key, val in dico.items():
        if val in rdico:
            print("Error, keys list has duplicates.")
            return None
        else:
            rdico.update({val:key})
    return rdico