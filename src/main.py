import random

TARGET_NUM = 1000 #Goal

class cell():
    def __init__(self):
        self.ftion = ['x','x','x','x','x','x','x']
        self.fstring = "XXXXXXX"
        self.value = -0.000000
        self.egradient = TARGET_NUM - self.value
        self.mutated = False

    def getRandomN(self):
        return str(random.randint(1, 100))

    def getRandomO(self):
        x = random.randint(1, 5)
        if x == 1:
            return '+'
        if x == 2:
            return '-'
        if x == 3:
            return '*'
        if x == 4:
            return '/'
        if x == 5:
            return '%'

    def updateF(self):
        self.fstring = ''.join(self.ftion)
        self.value = eval(self.fstring)
        if (self.value < 1):
            self.egradient = TARGET_NUM + (-1 * self.value)
        else:
            self.egradient = TARGET_NUM - self.value
        if (self.egradient < 1):
            self.egradient *= -1

    def generateF(self):
        iters = 0
        while iters < 7:
            if(iters % 2 == 0):
                self.ftion[iters] = cell.getRandomN(None)
            elif(iters % 2 != 0):
                self.ftion[iters] = cell.getRandomO(None)
            iters+=1
        self.updateF()

def reproduce(cell1, cell2):
    newcell = cell()
    crossover = random.randint(2,5)
    #mutation crap
    mutation = random.randint(1, 1000)
    mutationN = random.randint(0,6)
    iters = 0
    while(iters < 7):
        if(iters <= crossover):
            newcell.ftion[iters] = cell1.ftion[iters]
        elif(iters>crossover and mutation <= 10 and iters == mutationN):#mutate
            if (iters % 2 == 0):
                newcell.ftion[iters] = cell.getRandomN(None)
                newcell.mutated = True
            elif (iters % 2 != 0):
                newcell.ftion[iters] = cell.getRandomO(None)
        elif (iters > crossover):
            newcell.ftion[iters] = cell2.ftion[iters]
        iters+=1
    newcell.updateF()
    return newcell

def reptwice(celllist, cell1, cell2):
    celluno = reproduce(cell1, cell2)
    celldos = reproduce(cell2, cell1)
    celllist.append(celluno)
    celllist.append(celldos)

def bubosort(cell_list):
    swapped = False
    while(not swapped):
        swapped = True
        for x in range(1, 20):

            if (cell_list[x-1].egradient > cell_list[x].egradient):

                tempcell = cell_list[x]
                cell_list[x] = cell_list[x - 1]
                cell_list[x - 1] = tempcell

                swapped = False



celldad = cell()
celldad.generateF()
print("TARGET VALUE: ", TARGET_NUM, "\n Cell Dad:")
print(celldad.ftion, "=", celldad.value)
print("error gradient: ", celldad.egradient)
print("mutated? ", celldad.mutated)

cellmom = cell()
cellmom.generateF()
print("\n Cell Mom:\n",cellmom.ftion, "=", cellmom.value)
print("error gradient: ", cellmom.egradient)
print("mutated? ", celldad.mutated)

child = reproduce(celldad, cellmom)
print("\n Child:\n", child.ftion, "=", child.value)
print("error gradient: ", child.egradient)
print("mutated? ", celldad.mutated)



def main():
    GEN_LIMIT = 10000
    running = True
    generations = 0
    cellpool = []
    fitnesspool = []
    birthpool = []
    parents = []

    poolscreenshot = []

    while(running == True and generations < GEN_LIMIT):

        print("\n======[GENERATION ", generations + 1, "]======")
        if(generations == 0):
            for x in range(0, 20):
                placeholder = cell()
                placeholder.generateF()
                cellpool.append(placeholder)
            for x in range(0, 20):
                print("Cell ", x + 1 + (generations - 1) * 10, cellpool[x].ftion, "=", cellpool[x].value, " eG: ",
                        cellpool[x].egradient)
        bubosort(cellpool)#sort cellpool
        #move important cells to fitness pool, halve population
        for x in range(0,10):
            fitnesspool.append(cellpool[x])
            parents.append(cellpool[x])
        #diversity is good, here's some invasions:
        if generations % 10 == 0:
            if(poolscreenshot == cellpool):
                survivors = fitnesspool[0]
                fitnesspool.clear()
                for x in range(0, 10):
                    placeholder = cell()
                    placeholder.generateF()
                    fitnesspool.append(placeholder)
                for x in range(5, 10):
                    fitnesspool[x] = survivors
            poolscreenshot = cellpool
        #diversity end // comment out for no invasions

        #reproduce and fill birthpool
        y = 2
        for x in range(0,10):
            if(x == 0):#the x could cause confusion here but I'm just using it as an iterator
                for x in range(0, 2):
                    for g in range (0, 10):
                        reptwice(birthpool, fitnesspool[0], fitnesspool[g])
            elif(x == 1):
                for x in range(1, 8):
                    reptwice(birthpool, fitnesspool[1], fitnesspool[random.randint(2,9)])
            else:
                for g in range(1, 4):
                    reptwice(birthpool, fitnesspool[x], fitnesspool[random.randint(x, 9)])
                    y+=1
        #clear fitnesspool, sort birthpool and re-populate cellpool after clear
        fitnesspool.clear()
        bubosort(birthpool)

        cellpool.clear()
        for x in range(0, 10):#refil cellpool with birthpool / change from 10 to 20 and remove parents append for no possible incest
            cellpool.append(birthpool[x])
        for x in range(10, 20):
            cellpool.append(parents[x-10])
        #possible incest end

        for x in range(0, 20):
            if(cellpool[x].egradient == 0):
                running = False

        bubosort(cellpool)#sort cellpool again
        if(generations == 0):
            print("\n======[GENERATION ", generations + 2, "]======")

        for x in range(0, 20):
            print("Cell ", x+1,cellpool[x].ftion,"=" ,cellpool[x].value, " eG: ",cellpool[x].egradient)

        birthpool.clear()
        generations+=1

if __name__ == '__main__':
    main()