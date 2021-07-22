import random
import time
import math
from rectangle import Rectangle

class Insertion:
    #constructor
    def __init__(self):
        self.type = "INSERTION SORT"
        self.complexity = "O(n^2)"
        self.background = (100, 0, 0)
        self.comparisons = 0
        self.swaps = 0
        self.curIndex = -1

        repeat = .1
        rectList = []
        for i in range(1, 101):
            red   = math.sin(repeat*i + 0) * 127 + 128
            green = math.sin(repeat*i + 2) * 127 + 128
            blue  = math.sin(repeat*i + 4) * 127 + 128
            rectList.append(Rectangle((red, green, blue), i))
        self.nums = rectList
        random.shuffle(self.nums)

    def sort(self):
        for i in range(1, len(self.nums)):
            inserted = False
            j = i
            while (not inserted):
                self.curIndex = j
                if (self.nums[j].height < self.nums[j-1].height):
                    temp = self.nums[j]
                    self.nums[j] = self.nums[j-1]
                    self.nums[j-1] = temp
                    self.swaps+=1
                    self.curIndex = j-1
                    if (self.curIndex == 0):
                        inserted = True
                else:
                    inserted = True
                self.comparisons+=1
                import display
                display.updateAlgo(self)
                j -= 1
        time.sleep(5)

