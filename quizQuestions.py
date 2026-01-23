def questionThree():
    grade = (int(input('Grade \n :> ')) / 10)
    letterGrades = ['A', 'B', 'C', 'D', 'F']
    i = 10
    while (i > grade) and (i >= 6):
        i = i - 1
    print(letterGrades[9 - i])


questionThree()
