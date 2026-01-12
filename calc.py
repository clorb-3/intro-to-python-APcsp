print('calc *vars not supported')
equation = list(input(':> '))
print(equation)


def isolateParinthsis(inputEquation):
    if '(' and ')' in inputEquation:
        indexOfClosed = inputEquation.index(')')
        indexOfOpen = indexOfClosed
        while inputEquation[indexOfOpen] != '(':
            indexOfOpen = indexOfOpen - 1
        subEquation = inputEquation[indexOfOpen:indexOfClosed + 1]
        print(subEquation)


isolateParinthsis(equation)
