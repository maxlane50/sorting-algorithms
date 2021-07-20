import random
import time

class Bubble:
    #constructor
    def __init__(self):
        self.type = "BUBBLE SORT"
        self.complexity = "O(n^2)"
        self.background = (42, 45, 118)
        self.nums = list(range(1,101))
        random.shuffle(self.nums)
        self.comparisons = 0
        self.swaps = 0
        self.curIndex = -1

    #sorting algo
    def sort(self):
        for i in range(len(self.nums)):
            for j in range (len(self.nums)-i-1):
                if (self.nums[j+1] < self.nums[j]):
                    temp = self.nums[j]
                    self.nums[j] = self.nums[j+1]
                    self.nums[j+1] = temp
                    self.swaps+=1
                self.comparisons+=1
                self.curIndex = j
                import display
                display.updateAlgo(self)
        time.sleep(3)
