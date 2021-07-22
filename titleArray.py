import random
import time

class TitleArray:
    def __init__(self):
        self.array = []
        for i in range(25):
            self.array.append(TitleArrayVal())
    
    def mix(self):
        for i in range(2):
            idxToSwitch = random.randrange(0,25)
            self.array[idxToSwitch] = TitleArrayVal()

        #self.array = []
        #for i in range(25):
        #    self.array.append(random.randrange(0,10))

class TitleArrayVal:
    def __init__(self):
        self.value = random.randrange(0,10)
        r = random.randrange(30, 220)
        g = random.randrange(30, 220)
        b = random.randrange(30, 220)
        self.color = (r, g, b)