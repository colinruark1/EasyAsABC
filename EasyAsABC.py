class Cell:
    # Initiation using an x coordinate, y coordinate, and the letter
    def __init__(self, x, y, letter):
        self.xv = x
        self.yv = y
        self.t = letter
        self.buff = None

    #Getter functions
    def getX(self):
        return self.xv

    def getY(self):
        return self.yv
    def getType(self):
        return (self.t)

def gridX(num):
    return (num % 6)

def gridY(num):
    return (num // 6)

# Inputs a substring, Outputs the integer value that the substring represents
# Preconditions:
#   first character in the string is a number
#   number is of length 1 or of length 2
# Postconditions:
# Integer is outputted that represents the first number in inputted String
def stringInt(s):
    val = 0
    if(len(s) > 2):
        s = s[:s.find(",")]
    if(len(s) == 2):
        val += ((ord(s[0]) - 48) * 10)
        val += (ord(s[1]) - 48)
    elif(len(s) == 1):
        val = (ord(s) - 48)
    return val

#Inputs a location value 0-35 and outpu
def final_answer(y, st):
    for i in range(5 + (2 * numFirstFound(st))):
        st = st[(st.find(",")) + 2:]
    loc = stringInt(st) - 1
    print(y[gridY(loc)][gridX(loc)])

#Finds the first 4 'x' blocks
def blocks(s):
    x = []
    for i in range(4):
        x += [stringInt(s) - 1]
        s = s[(s.find(",")) + 2:]
    return x

# amount of data to begin chart
def numFirstFound(s):
    for i in range(4):
        s = s[(s.find(",")) + 2:]
    return stringInt(s[:1])

# adds the 4 'x' blocks to the greater array of objects
def addBlocks(cells, st):
    inp = Cell(0, 0, "X")
    for j in range(len(blocks(st))):
        inp = Cell(blocks(st)[j] % 6, blocks(st)[j] // 6, "X")
        cells += [inp]
    return cells

# boolean value for if a given coordinate is already assigned to a letter within cells
def cellFound(cells, num):
    found = False
    for cell in cells:
        if (Cell.getX(cell) == gridX(num) and Cell.getY(cell) == gridY(num)):
            found = True
    return found

# input the start data into the list of cells
def inputFirstFound(cells, st):
    a = ""
    b = 0
    loc = 0
    nff = numFirstFound(st)
    for i in range(5):
        st = st[(st.find(",")) + 2:]
    for j in range(nff):
        a = st[0]
        st = st[(st.find(",")) + 2:]
        b = (stringInt(st[:st.find(",")])) - 1
        st = st[(st.find(",")) + 2:]
        cells += [Cell(gridX(b), gridY(b), a)]
        loc = b
        if(gridX(b) == 0):
            notFound = True
            while(notFound):
                loc += 1
                if (not cellFound(cells, loc)):
                    cells += [Cell(gridX(loc), gridY(loc), a)]
                    notFound = False
        elif(gridX(b) == 5):
            notFound = True
            while (notFound):
                loc -= 1
                if (not cellFound(cells, loc)):
                    output = Cell(gridX(loc), gridY(loc), a)
                    cells += [Cell(gridX(loc), gridY(loc), a)]
                    notFound = False
    return cells

# Input: Entire y[] grid
# Output: True if grid is filled, False if not
def filled(y):
    isFilled = True
    for i in range(4):
        for j in range(4):
            if(y[j+1][i+1] == "-"):
                isFilled = False
    return isFilled

def oneDashFill(y):
    base = ""
    for i in range(4):
        base = "ABCX"
        (x, z) = (0, 0)
        for j in range(4):
            if (base.find(y[i + 1][j + 1]) != -1):
                base = base.replace(y[i + 1][j + 1], "")
            else:
                (x, z) = (i + 1, j + 1)
        if (len(base) == 1):
            y[x][z] = base
    for j in range(4):
        base = "ABCX"
        (x, z) = (0, 0)
        for i in range(4):
            if (base.find(y[i + 1][j + 1]) != -1):
                base = base.replace(y[i + 1][j + 1], "")
            else:
                (x, z) = (i + 1, j + 1)
        if (len(base) == 1):
            y[x][z] = base
    return y

def twoDashFill(y):
    for i in range(4):
        base = "ABCX"
        x = []
        z = []
        for j in range(4):
            if (base.find(y[i + 1][j + 1]) != -1):
                base = base.replace(y[i + 1][j + 1], "")
            else:
                x.append(i + 1)
                z.append(j + 1)
        if(len(base) == 2):
            for k in range(4):
                if(base.find(y[k + 1][z[0]]) != -1):
                    base = base.replace(y[k + 1][z[0]], "")
            if(len(base) == 1):
                y[x[0]][z[0]] = base
                oneDashFill(y)
    for j in range(4):
        base = "ABCX"
        x = []
        z = []
        for i in range(4):
            if (base.find(y[i + 1][j + 1]) != -1):
                base = base.replace(y[i + 1][j + 1], "")
            else:
                x.append(i + 1)
                z.append(j + 1)
        if (len(base) == 2):
            for k in range(4):
                if (base.find(y[x[0]][k + 1]) != -1):
                    base = base.replace(y[x[0]][k + 1], "")
            if (len(base) == 1):
                y[x[0]][z[0]] = base
                oneDashFill(y)
    return y

def fill(y):
    while(not filled(y)):
        oneDashFill(y)
        twoDashFill(y)
    return y



def main():
    #Making a list of all filled cells using input data
    cells = []

    #Building the grid
    y = [["-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-"]]

    #Assuming a valid input with a sufficient set of values
    st = input('Please input a String.\n')
    cells = addBlocks(cells, st)
    cells += inputFirstFound(cells, st)
    cell = Cell(0, 0, "X")

    #Taking all cells from input data and inputting them into y[]
    for k in range(len(cells)):
        cell = cells[k]
        y[Cell.getY(cell)][Cell.getX(cell)] = Cell.getType(cell)
    y = fill(y)

    #Display of filled grid
    for i in range(6):
        print(y[i])

    final_answer(y, st)

if __name__ == '__main__':
    #Multiple runs to test edge cases
    for i in range(5):
        main()