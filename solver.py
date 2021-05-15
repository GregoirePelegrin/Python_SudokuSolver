import MaskLib

data = []
groups = []
pool = []
possibilities = []

def display():
    soluce = ""
    size = int(len(pool) ** 0.5)
    for i,line in enumerate(data):
        if i != 0 and i % size == 0: 
            for j in range(len(pool)*2 + 3*(size-1) - 1):
                soluce += "="
            soluce += "\n"
        for j,cell in enumerate(line):
            if j != 0 and j % size == 0: soluce += "|| "
            soluce += "{}".format(cell)
            if j != len(line)-1: soluce += " "
        if i != len(data)-1: soluce += "\n"
    print(soluce)
def displayPossibilities():
    poss = ""
    size = int(len(pool) ** 0.5)
    for i,line in enumerate(possibilities):
        if i != 0 and i % size == 0: 
            for j in range(len(pool)*(len(pool)+4) + 3*(size-1) - 1):
                poss += "="
            poss += "\n"
        for j,cell in enumerate(line):
            if j != 0 and j % size == 0: poss += "|| "
            if type(cell) == int:
                for k in range(int(len(pool)/2)): poss += " "
                poss += "{}(i)".format(cell)
                for k in range(int(len(pool)/2)): poss += " "
            else: 
                for k in range(int((len(pool)-len(cell))/2)): poss += " "
                for c in cell: poss += "{}".format(c)
                poss += "(l)"
                if len(cell) % 2 == 0: poss += " "
                for k in range(int((len(pool)-len(cell))/2)): poss += " "
            poss += " "
        if i != len(possibilities)-1: poss += "\n"
    print(poss)
def fillPossibilities():
    for line in data:
        temp = []
        for cell in line:
            if cell == 0:
                temp.append(pool[:])
            else:
                temp.append(cell)
        possibilities.append(temp)
def getInitialState(filename):
    with open(filename, "r") as f:
        content = f.read()
    content = content.split("\n")
    for line in content:
        temp = []
        for cell in line:
            try:
                temp.append(int(cell))
            except:
                temp.append(0)
        data.append(temp)
def groupGeneration():
    groups.clear()
    for i in range(len(pool)):
        line = []
        col = []
        for j in range(len(pool)):
            line.append([i, j])
            col.append([j, i])
        groups.append(line)
        groups.append(col)
    size = int(len(pool) ** 0.5)
    for i in range(size):
        for j in range(size):
            block = []
            for k in range(size):
                for l in range(size):
                    block.append([i*size+k, j*size+l])
            groups.append(block)
def poolGeneration():
    for i in range(1, len(data)+1):
        pool.append(i)
def solve():
    solved = False
    while not solved:
        updatePossibilities()
        updateData()
        solved = True
        for line in data:
            if 0 in line:
                solved = False
                break
def updateData():
    for i in range(len(pool)):
        for j in range(len(pool)):
            if type(possibilities[i][j]) != int and len(possibilities[i][j]) == 1:
                data[i][j] = possibilities[i][j][0]
def updatePossibilities():
    for group in groups:
        mask = MaskLib.Mask(_s=len(pool))
        while not mask.maxed:
            mask.increment()
            isComplete, possExposed = verifExposed(mask, group)
            if isComplete:
                for bit,g in zip(mask.value, group):
                    if bit == "0":
                        for poss in possExposed:
                            try:
                                possibilities[g[0]][g[1]].remove(poss)
                            except:
                                pass
def verifExposed(mask, g):
    temp = []
    for i,bit in enumerate(mask.value):
        if bit == "1": temp.append(possibilities[g[i][0]][g[i][1]])
    possSet = []
    for cell in temp:
        if type(cell) == int:
            if cell not in possSet: possSet.append(cell)
            continue
        for poss in cell:
            if poss not in possSet: possSet.append(poss)
    return (len(possSet) == mask.exposed, possSet)

getInitialState("data.txt")
poolGeneration()
groupGeneration()

fillPossibilities()

solve()
display()