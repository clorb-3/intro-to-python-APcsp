def countDown():
    for i in range(10):
        print(str(10 - i))


def countDownTwo():
    i = 10
    while i != 0:
        print(str(i))
        i = i - 1


def printComputer():
    word = 'computer'
    for i in range(len(word)):
        print(word[i])


def printComputerTwo():
    word = 'computer'
    for i in word:
        print(i)


countDown()
countDownTwo()
printComputer()
printComputerTwo()
