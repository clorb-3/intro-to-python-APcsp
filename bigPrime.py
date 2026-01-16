def getNines(diget):
    output = 9
    i = 1
    while i != diget:
        output = output * 10
        output = output + 9
        i = i + 1
    return (output)


def biggestPrime(maxNum):
    test = maxNum
    prime = False
    while prime is False:
        test = test - 1
        prime = isPrime(test)
        if test < 0:
            prime = True
    return (test)


def isPrime(num):
    test = 1
    factors = 0
    numRoot = getNiceRoot(num)
    while test < numRoot:
        test = test + 1
        if num % test == 0:
            factors = factors + 1
    if factors == 0:
        return (True)
    else:
        return (False)


def getNiceRoot(num):
    numRoot = num ** 0.5
    numRoot = numRoot + 1
    numRoot = numRoot.real
    return (numRoot)


print(biggestPrime(getNines(int(input('biggest __ diget prime\n:>')))))
# print(isPrime(7))
