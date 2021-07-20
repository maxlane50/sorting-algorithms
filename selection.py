import random
import time

class Selection:
    #constructor
    def __init__(self):
        self.type = "Selection Sort"
        self.nums = list(range(1,101))
        random.shuffle(self.nums)
        self.comparisons = 0
        self.swaps = 0

    #sorting algo
    def sort(self):
        for i in range(len(self.nums)):
            min = self.nums[i]
            minIndex = i
            for j in range (i+1, len(self.nums)):
                if (self.nums[j] < min):
                    min = self.nums[j]
                    minIndex = j
                self.comparisons += 1
                import display
                display.updateSelection(self, j, minIndex)
            temp = self.nums[i]
            self.nums[i] = self.nums[minIndex]
            self.nums[minIndex] = temp
            self.swaps += 1
        time.sleep(3)
