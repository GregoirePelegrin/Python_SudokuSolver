data = []
groups = []
pool = []
possibilities = []

def display():
    soluce = ""
    size = int(len(pool) ** 0.5)
    for i,line in enumerate(data):
        if i != 0 and i % size == 0: soluce += "=======================\n"
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
        if i != 0 and i % size == 0: poss += "==========================================================================================================================\n"
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
        # print("Current possibilities:")
        # displayPossibilities()
        # print("Current data:")
        # display()
        solved = True
        for line in data:
            if 0 in line:
                solved = False
                break
        # if input("Continue? (y/n) ") == "n":
        #     break
def updateData():
    for i in range(len(pool)):
        for j in range(len(pool)):
            if type(possibilities[i][j]) != int and len(possibilities[i][j]) == 1:
                data[i][j] = possibilities[i][j][0]
def updatePossibilities():
    for group in groups:
        verifGroup(group)
def verifGroup(g):
    for i in range(len(g)):
        content = possibilities[g[i][0]][g[i][1]]
        if type(content) == int:
            for j in range(len(g)):
                try:
                    possibilities[g[j][0]][g[j][1]].remove(content)
                except:
                    pass
            continue
        count = 1
        for j in range(len(g)):
            if i != j and content == possibilities[g[j][0]][g[j][1]]: 
                count += 1
        if len(content) == count:
            for j in range(len(g)):
                if content != possibilities[g[j][0]][g[j][1]]:
                    for c in content:
                        try:
                            possibilities[g[j][0]][g[j][1]].remove(c)
                        except:
                            pass
        for c in content:
            alone = True
            for j in range(len(g)):
                if i != j and type(possibilities[g[j][0]][g[j][1]]) != int and c in possibilities[g[j][0]][g[j][1]]:
                    alone = False
                    break
                if type(possibilities[g[j][0]][g[j][1]]) == int and c == possibilities[g[j][0]][g[j][1]]:
                    alone = False
                    break 
            if alone:
                possibilities[g[i][0]][g[i][1]] = [c]
                break

getInitialState("data2.txt")
poolGeneration()
groupGeneration()

fillPossibilities()

solve()
display()