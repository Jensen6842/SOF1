#Exercise 1

a_word = "lol"
f = open("exo1.txt",'w')
f.write(a_word)
f.close()

#Exercise 2

def save_list2file(sentences, filename):
    f = open(filename,'a')
    for word in sentences:
        f.write(word + '/n')
    f.close()

#Exercise 3

def save_to_log(entry, logfile):
    f = open(logfile,'a')
    f.write(entry)
    f.close()

#Exercise 4

f = open("exo1.txt",'r')
lines = f.readlines()
for line in lines:
    print(line.upper())
f.close()

#Exercise 5

def to_upper_case(input_file, output_file):
    f = open(input_file,'r')
    temp = f.readlines()
    f.close()
    f = open(output_file,'w')
    f.write(temp)
    f.close()

#Exercise 6

#error questions here

def sum_numbers(a_string):
    nums = a_string.split()
    sum = 0
    for num in nums:
        sum += int(num)
    return sum

def sum_from_file(filename):
    f = open(filename,'r')
    sum = 0
    lines = f.readlines()
    for i in lines:
        sum += sum_numbers(i)
    f.close()
    return sum