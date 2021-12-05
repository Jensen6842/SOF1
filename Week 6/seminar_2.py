def listSum(list):
    highest = 0
    for start in range(len(list)):
        for end in range(len(list)):
            if sum(list[start:end+1]) > highest:
                highest = sum(list[start:end+1])
    return highest

sublist = [[6, -5, -7, 4, -4],[-9, 3, -6, 5, 2],[-10, 4, 7, -6, 3],[-8, 9, -3, 3, -7]]

def martixSum(sublist):
    currentmax = 0
    for sublistheight in range(1, len(sublist) + 1):
        for sublistwidth in range(1, len(sublist[0]) + 1):
            for rowindex in range(0, len(sublist) + 1 - sublistheight):
                for columnindex in range(0, len(sublist[0]) + 1 - sublistwidth):
                    newmax = 0
                    for sublistrow in range(0, sublistheight):
                        for sublistcolumn in range(0, sublistwidth):
                            newmax += sublist[rowindex + sublistrow][columnindex + sublistcolumn]
                    if newmax > currentmax:
                        currentmax = newmax
    print("Maximum contiguous sum is",currentmax)
    return

martixSum(sublist)