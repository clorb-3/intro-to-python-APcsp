import random
blankSpace = '                                         '


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
    guarantee = 10 ** 14
    if num < guarantee:
        numRoot = getNiceRoot(num)
        if num % 2 == 0:
            return (False)
        while (test < numRoot):
            test = test + 2
            print(str(num) + '/' + str(test) + '   ', end='\r')
            if num % test == 0:
                return (False)
        if num < guarantee:
            return (True)
    print('Miller Rabin Test *', end='\r')
    return (miller_rabin(num, 50))


def getNiceRoot(num):
    numRoot = num ** 0.5
    numRoot = numRoot + 1
    numRoot = numRoot.real
    return (numRoot)


def miller_rabin(n, k):  # A python version of the Miller Rabin Primality test
    # made by made by https://gist.github.com/Ayrx
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        print('Miller Rabin Test ' +
              str(round(((_ + 1) / k) * 100)) + '%  ', end='\r')
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def getBiggestPrime():
    digits = int(input('biggest __ digit prime\n:> '))
    maxNum = getNines(digits)
    prime = biggestPrime(maxNum)
    print('\n' + str(prime))


# print(str(biggestPrime(getNines(int(input('biggest __ diget prime\n:>'))))))
getBiggestPrime()
