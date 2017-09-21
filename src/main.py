import random

TARGET_NUM = 42.0 #Goal

class cell():
    ftion = ['x','x','x','x','x','x','x']
    fstring = "XXXXXXX"
    value = -0.000000
    egradient = TARGET_NUM - value

    def getRandomN(self):
        return str(random.randint(1, 100))

    def getRandomO(self):
        x = random.randint(1, 4)
        if x == 1:
            return '+'
        if x == 2:
            return '-'
        if x == 3:
            return '*'
        if x == 4:
            return '/'

    def generateF(self):
        iters = 0;
        while iters < 7:
            if(iters % 2 == 0):
                cell.ftion[iters] = cell.getRandomN(None)
            elif(iters % 2 != 0):
                cell.ftion[iters] = cell.getRandomO(None)
            iters+=1
        cell.fstring = ''.join(cell.ftion)
        cell.value = eval(cell.fstring)
        if (cell.value < 1):
            cell.egradient = TARGET_NUM + (-1 * cell.value)
        else:
            cell.egradient = TARGET_NUM - cell.value
        if(cell.egradient < 1):
            cell.egradient *= -1


newcell = cell()
newcell.generateF()
print("TARGET VALUE: ", TARGET_NUM)
print(newcell.ftion,"=", newcell.value)
print("error gradient: ", newcell.egradient)
