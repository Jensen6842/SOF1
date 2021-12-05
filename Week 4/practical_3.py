#Exercise 1

def sum_digits(number):
    sumd = 0
    for i in str(number):
        sumd += int(i)
    return sumd

print(sum_digits(int(input("positive number: "))))

#Exercise 2

def pairwise_digits(number_a, number_b):
    if len(number_a) >= len(number_b):
        longest = number_a
        shortest = number_b
    else:
        shortest = number_a
        longest = number_b
    output = ""
    shortest = shortest + ("0" * (len(longest) - len(shortest)))
    for chars in range(len(shortest)):
        if shortest[chars] == longest[chars]:
            output = output + "1"
        else:
            output = output + "0"
    return output

number_a = input("positive number: ")
number_b = input("positive number: ")
print(pairwise_digits(number_a, number_b)

#Exercise 3

def to_base10(binary):
    binary = binary[::-1]
    denary = 0
    for i in range(len(binary)):
        denary += int(binary[i])*(2**i)
    return denary

binary = input("binary number: ")
print(to_base10(binary))

#Exercise 4

def triangle(rows):
    row = ""
    for i in range(rows):
        if i%2 == 0:
            row += "1"
        else:
            row += "0"
        print(row[::-1])

rows = int(input("number of rows: "))
triangle(rows)

#Exercise 5

def sum_lists(list_2D):
    output = []
    for row in list_2D:
        total = 0
        for val in row:
            total += val
        output.append(total)
    return output

data = [[1,2,3], [2], [1,2,3,4]]
print(sum_lists(data))