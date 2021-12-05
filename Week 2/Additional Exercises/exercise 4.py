age = int(input("What is your age? "))
rate = float(input("What is your heart rate? "))
m = 208 - (0.7 * age)
if rate >= (0.9 * m):
    print("Interval training")
elif rate >= (0.7 * m):
    print("Threshhold training")
elif rate >= (0.5 * m):
    print("Aerobic training")
else:
    print("Couch potato")
