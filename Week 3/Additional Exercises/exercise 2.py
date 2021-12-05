numlist = []
for x in range(4):
    tempnumlist = input(">>> enter 4 digits (0..4) seperated by a space: ").split()
    for i in range(0, len(tempnumlist)):
        tempnumlist[i] = int(tempnumlist[i])
    numlist.append(tempnumlist)

for x in range(4):
    for i in range(4):
        if numlist[x][i] == 0:
            numlist[x][i] = " "
    print("+-+-+-+-+\n|" + str(numlist[x][0]) + "|" + str(numlist[x][1]) + "|" + str(numlist[x][2]) + "|" + str(numlist[x][3]) + "|")
print("+-+-+-+-+")
