import random
import time
import math
from rectangle import Rectangle

class Bubble:
    #constructor
    def __init__(self):
        self.type = "BUBBLE SORT"
        self.complexity = "O(n^2)"
        self.background = (42, 45, 118)
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

    #sorting algo
    def sort(self):
        for i in range(len(self.nums)):
            for j in range (len(self.nums)-i-1):
                if (self.nums[j+1].height < self.nums[j].height):
                    temp = self.nums[j]
                    self.nums[j] = self.nums[j+1]
                    self.nums[j+1] = temp
                    self.swaps+=1
                self.comparisons+=1
                self.curIndex = j
                import display
                display.updateAlgo(self)
        time.sleep(5)
