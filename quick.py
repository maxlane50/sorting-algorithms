import random
import time
import math
from rectangle import Rectangle

class Quick:
    #constructor
    def __init__(self):
        self.type = "QUICK SORT"
        self.complexity = "O(nlog(n))"
        self.background = (0, 77, 92)
        self.comparisons = 0
        self.swaps = 0
        self.curIndex = -1
        self.firstCall = True

        self.i = 100
        self.j = 100
        self.pivot = 100

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
    def sort(self, start, end):
        if self.firstCall:
            start = 0
            end = len(self.nums) - 1
            self.firstCall = False
        if start < end:
            breakPoint = self.divide(start, end)
            self.sort(start, breakPoint - 1)
            self.sort(breakPoint + 1, end)

    def divide(self, start, end):
        pivot = -69
        if (((end - start) + 1) % 2) == 0:
            index = end - ((end - start - 1)/2)
            index = int(index)
            pivot = self.nums[index].height
            self.pivot = index
        else:
            index = end - ((end - start)/2)
            index = int(index)
            pivot = self.nums[index].height
            self.pivot = index
        i = start
        j = end
        pauseI = False
        pauseJ = False
        while i < j:
            if (self.nums[i].height >= pivot):
                pauseI = True
            if (self.nums[j].height <= pivot):
                pauseJ = True
            if (pauseI and pauseJ):
                temp = self.nums[i]
                self.nums[i] = self.nums[j]
                self.nums[j] = temp
                self.swaps+=1
                pauseJ = False
                pauseI = False
            elif pauseI:
                j -= 1
            elif pauseJ:
                i += 1
            else:
                j -= 1
                i += 1
            self.i = i
            self.j = j

            import display
            display.updateAlgo(self)
        return i

