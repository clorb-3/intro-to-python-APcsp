value = 0
while True:
    value = value + 1
    output = str(value) + ' '
    if value % 3 == 0:
        output = output + 'Fizz'
    if value % 5 == 0:
        output = output + 'Buzz'
    print(output)
