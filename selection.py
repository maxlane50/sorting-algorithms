import random
import time

class Selection:
    #constructor
    def __init__(self):
        self.type = "SELECTION SORT"
        self.complexity = "O(n^2)"
        self.background = (0, 80, 0)
        self.minIndex = -1
        self.curIndex = -1
        self.nums = list(range(1,101))
        random.shuffle(self.nums)
        self.comparisons = 0
        self.swaps = 0

    #sorting algo
    def sort(self):
        for i in range(len(self.nums)):
            min = self.nums[i]
            self.minIndex = i
            for j in range (i+1, len(self.nums)):
                if (self.nums[j] < min):
                    min = self.nums[j]
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
