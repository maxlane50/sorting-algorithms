import random

class Bubble:
    #constructor
    def __init__(self):
        self.type = "Bubble Sort"
        self.nums = list(range(1,100))
        random.shuffle(self.nums)
        print(self.nums)
        self.comparisons = 0
        self.swaps = 0

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
                import display
                display.updateBubble(self, j)
