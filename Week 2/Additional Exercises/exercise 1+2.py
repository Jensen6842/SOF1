wc = 0.4535924
dc = 0.0254
lc = 0.4731765

def witm():
    stones = int(input("Stones: "))
    pounds = float(input("Pounds: "))
    pounds = stones*14 + pounds
    kg = pounds*wc
    print(kg, "Kilograms")
    return

def ditm():
    feet = int(input("Feet: "))
    inches = float(input("Inches: "))
    inches = feet*12 + inches
    meters = inches*dc
    print(meters, "Meters")
    return

def litm():
    gallons = int(input("Gallons: "))
    pints = float(input("Pints: "))
    pints = gallons*8 + pints
    litres = pints*lc
    print(litres, "Litres")
    return

def wmti():
    kg = float(input("Kilograms: "))
    pounds = int(kg//wc)
    stones = int(pounds//14)
    pounds = pounds - stones*14
    print(stones, "Stones", pounds, "Pounds")
    return

def dmti():
    meters = float(input("Meters: "))
    inches = int(meters//dc)
    feet = int(inches//12)
    inches = inches - feet*12
    print(feet, "Feet", inches, "Inches")
    return

def lmti():
    litres = float(input("Litres: "))
    pints = int(litres//lc)
    gallons = int(pints//8)
    pints = pints - gallons*8
    print(gallons, "Gallons", pints, "Pints")
    return
