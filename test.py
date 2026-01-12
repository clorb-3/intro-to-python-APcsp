itrationCount = int(input('count to: '))
numCount = 1


def iterate():
    global numCount
    global isOdd
    global isEven
    isOdd = str(numCount) + ' is odd\n'
    isEven = str(numCount + 1) + ' is even'
    print(isOdd + isEven)
    numCount = numCount + 2


while numCount < itrationCount:
    iterate()
