print('calc *vars not supported')
equation = list(input(':> '))
print(equation)
oporators = ['^', '*', '/', '+', '-']


def isolateParinthsis(inputEquation):
    if '(' and ')' in inputEquation:
        indexOfClosed = inputEquation.index(')')
        indexOfOpen = indexOfClosed
        while inputEquation[indexOfOpen] != '(':
            indexOfOpen = indexOfOpen - 1
        subEquation = inputEquation[indexOfOpen + 1:indexOfClosed]
        return (inputEquation, subEquation, indexOfOpen, indexOfClosed)
    else:
        return (inputEquation, subEquation, 0, len(inputEquation) - 1)


def doEquation(inputEquation, subEquation, indexOfOpen, indexOfClosed):
    print(inputEquation)
    del inputEquation[indexOfOpen:indexOfClosed]
    for item in oporators:
        while item in inputEquation:
            indexOfOperation = inputEquation.index(item)
            startOfOperation, endOfOperation = indexOfOperation
            while startOfOperation not in oporators:
                startOfOperation = startOfOperation - 1
            startOfOperation = startOfOperation + 1
            while endOfOperation not in oporators:
                endOfOperation = endOfOperation - 1
            endOfOperation = endOfOperation + 1
            print(inputEquation[startOfOperation:endOfOperation])
            anwser = doOperation(int(''.join(map(str, inputEquation[


def doOperation(firstNumGroup, operation, secondNumGroup):
    if operation == '^':
        anwser= firstNumGroup ** secondNumGroup
    elif operation == '*':
        anwser= firstNumGroup * secondNumGroup
    elif operation == '/':
        anwser= firstNumGroup / secondNumGroup
    elif operation == '+':
        anwser= firstNumGroup + secondNumGroup
    elif operation == '=':
        anwser= firstNumGroup - secondNumGroup
    return (list(str(anwser)))


doEquation(equation, 0, len(equation) - 1)
# while not (oporators in equation):
#     equation = doEquation(isolateParinthsis(equation))
