def sumnat():
    N = int(input("enter a positive integer. "))
    sumnat = 0
    for i in range(1, N+1):
        sumnat += i
    print("sumnat is", str(sumnat))

def multtable():
    N = int(input("enter a positive integer. "))
    for i in range(1, 13):
        print(str(i), "*", str(N), "is", str(i*N))

def fact():
    N = int(input("enter a positive integer. "))
    fact = 1
    for i in range(1, N+1):
        fact *= i
    print("fact is", str(fact))
