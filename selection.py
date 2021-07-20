import random
import time
import math
from rectangle import Rectangle

class Selection:
    #constructor
    def __init__(self):
        self.type = "SELECTION SORT"
        self.complexity = "O(n^2)"
        self.background = (0, 50, 0)
        self.minIndex = -1
        self.curIndex = -1
        self.comparisons = 0
        self.swaps = 0
        repeat = .1
        rectList = []
        for i in range(1, 101):
            red   = math.sin(repeat * i + 0) * 127 + 128
            green = math.sin(repeat * i + 2) * 127 + 128
            blue  = math.sin(repeat * i + 4) * 127 + 128
            rectList.append(Rectangle((red, green, blue), i))
        self.nums = rectList
        random.shuffle(self.nums)

    #sorting algo
    def sort(self):
        for i in range(len(self.nums)):
            min = self.nums[i].height
            self.minIndex = i
            for j in range (i+1, len(self.nums)):
                if (self.nums[j].height < min):
                    min = self.nums[j].height
                    self.minIndex = j
                self.comparisons += 1
                self.curIndex = j
                import display
                display.updateAlgo(self)
            temp = self.nums[i]
            self.nums[i] = self.nums[self.minIndex]
            self.nums[self.minIndex] = temp
            self.swaps += 1
        time.sleep(3)
