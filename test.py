itrationCount = int(input('count to: ')) + 2
numCount = 1


def iterate():
    global numCount
    global isOdd
    global isEven
    isOdd = str(numCount) + ' is odd\n'
    isEven = str(numCount + 2) + ' is even'
    print(isOdd + isEven)
    numCount = numCount + 2


while numCount < itrationCount:
    iterate()
