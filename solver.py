data = []
pool = []
possibilities = []

def getInitialState(filename):
    with open(filename, "r") as f:
        content = f.read()
    content = content.split("\n")
    for i in range(len(content)):
        content[i] = content[i].split(" ")
    for line in content:
        temp = []
        for cell in line:
            if cell == 'x':
                temp.append(0)
            else:
                temp.append(int(cell))
        data.append(temp)
def fillPossibilities():
    for line in data:
        temp = []
        for cell in line:
            if cell == 0:
                temp.append(pool[:])
            else:
                temp.append(cell)
        possibilities.append(temp)
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
    for i in range(len(data)):
        for j in range(len(data[i])):
            if type(possibilities[i][j]) != int and len(possibilities[i][j]) == 1:
                data[i][j] = possibilities[i][j][0]
def updatePossibilities():
    for i in range(len(data)):
        for j in range(len(data)):
            verifCell(i, j)
def verifCell(i, j):
    if type(possibilities[i][j]) != int:
        for cell in data[i]:
            try:
                possibilities[i][j].remove(cell)
            except:
                pass

        for line in data:
            try:
                possibilities[i][j].remove(line[j])
            except:
                pass
        
        size = int(len(data)**0.5)
        xMin = int(i / size) * size
        xMax = xMin + size
        yMin = int(j / size) * size
        yMax = yMin + size

        for x in range(xMin, xMax):
            for y in range(yMin, yMax):
                if x == i and y == j:
                    continue
                try:
                    possibilities[i][j].remove(data[x][y])
                except:
                    pass

getInitialState("data.txt")
poolGeneration()
# print("Data: {}\nPool: {}".format(data, pool))

fillPossibilities()
# print("Possibilities: {}".format(possibilities))

solve()
print("Data: {}".format(data))