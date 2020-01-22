import random

INITIAL_SIZE = 100

def mainLogic(puzzleList):
    length = len(puzzleList)
    firstSum = 0
    secondSum = 0
    
    for i in range(0, int((length / 2))):
        firstSum += puzzleList[i] * pow(-1, i)
        
    for i in range(int(length / 2),  length):
        secondSum += puzzleList[i] * pow(-1, i + 1)

    return firstSum >= secondSum

def compareEm(puzzleList):
    p1 = 0
    p2 = 0

    while len(puzzleList) > 0:
        p1 += puzzleList.pop(0) if mainLogic(puzzleList) else puzzleList.pop()
        p2 += puzzleList.pop(0) if bool(random.getrandbits(1)) else puzzleList.pop()

    return (p1, p2)

if __name__ == '__main__':
    iteration = 1
    errorCount = 0

    try:
        while True:
            puzzleList = random.sample(range(1, INITIAL_SIZE * 10), INITIAL_SIZE)

            values = compareEm(puzzleList[:])
            worked = values[0] >= values[1]
            output = f'{iteration}: {puzzleList} --> {values}, {worked}'
            # print(output)

            if not worked:
                errorCount += 1
                f = open('mistakes.txt', 'a+')
                f.write(output + '\n')

            iteration += 1
    except KeyboardInterrupt:
        print(f'The test ran {iteration} times and resulted in {errorCount} errors.')