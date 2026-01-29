superList = [9, 82, -1, 15, 2, 4, 3, 1, 3, 4, 6, 7, 10]


def isAllPositive(inList):
    for i in inList:
        if i < 0:
            return False
    return True


def greatestVal(inList):
    biggestVal = 0
    for i in inList:
        if i >= biggestVal:
            biggestVal = i
    return (biggestVal)


def multList(inList, multFactor):
    for i in range(len(inList)):
        inList[i] = inList[i] * 100
    return (inList)


def rotateList(inList):
    firstVal = inList[0]
    for i in range(len(inList) - 1):
        inList[i] = inList[(i + 1)]
    inList[len(inList) - 1] = firstVal
    return (inList)


print(str(superList))
print(str(isAllPositive(superList)))
print(str(greatestVal(superList)))
print(str(multList(superList, 100)))
print(str(rotateList(superList)))
