def getlist():
    num = 0
    numlist = []
    while num >= 0:  
        num = int(input("enter a number "))
        numlist.append(num)
    return numlist

def sumneg():
    numlist = getlist()
    print("sumneg is", str(sum(numlist)))

def avgneg():
    numlist = getlist()
    print("avgneg is", str(round(sum(numlist)/len(numlist))))

def evenneg():
    numlist = getlist()
    even = 0
    for i in numlist:
        if i%2 == 0:
            even += 1
    print("evenneg is", str(even))
