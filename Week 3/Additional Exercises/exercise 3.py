decimal = int(input("enter a positive integer: "))
binary = ""
while True:
    if decimal == 0:
        break
    binary = binary + str(decimal%2)
    decimal = decimal//2
print(binary[::-1])
