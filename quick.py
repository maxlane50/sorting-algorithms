import random
import time

class Quick:
    #constructor
    def __init__(self):
        self.type = "QUICK SORT"
        self.complexity = "O(nlog(n))"
        self.background = (0, 77, 92)
        self.nums = list(range(1,101))
        random.shuffle(self.nums)
        self.comparisons = 0
        self.swaps = 0
        self.curIndex = -1
        self.pivot = -1

    #sorting algo
    def sort(list):
        lower = []
        higher = []
        if (len(list) >= 2):
            pivot = list[len(list)-1]
            for i in range(len(list)):
                if (value < pivot):
                    lower.append(value)
                    self.comparisons+=1
                elif (value == pivot):
                    junk = 1
                    self.comparisons+=2
                else:
                    higher.append(value)
                    self.comparisons+=3
            return sort(lower) + pivot + sort(higher)
        else:
            return list














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