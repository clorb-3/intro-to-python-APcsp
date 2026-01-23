import random


def simCycle():
    winningDoor = random.randint(1, 3)
    choice = random.randint(1, 3)
    if choice != winningDoor:
        removedDoor = 6 - (choice + winningDoor)
    removedDoor = choice
    while choice == removedDoor:
        removedDoor = random.randint(1, 3)
    choice = 6 - (choice + removedDoor)
    if choice == winningDoor:
        return 1
    return 0


def runSimulation(iterations):
    i = 0
    wins = 0
    while i != iterations:
        print("Running: " + str(round(i / iterations * 100)) + "%", end='\r')
        wins = wins + simCycle()
        i = i + 1
    print("Swaped is winner " + str(wins) +
          "times. Stayed is winner " + str(iterations - wins) + "times")


runSimulation(int(input("Run door simulation __ times \n :> ")))
