numlist = input(">>> enter a series of numbers: ").split()
even = 0
evens = ""
nums = []
for i in numlist:
    i = int(i)
    if i in nums:
        continue
    nums.append(i)
    if i % 2 == 0:
        even += 1
        evens = evens + " " + str(i)
print("There are", str(even), "distinct even numbers:" + evens)
