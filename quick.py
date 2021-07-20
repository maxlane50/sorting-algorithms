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
    def sort2(self, list):
        lower = []
        higher = []
        if (len(list) >= 2):
            pivot = list[len(list)-1]
            for i in range(len(list)):
                if (list[i] < pivot):
                    lower.append(list[i])
                    self.comparisons+=1
                elif (list[i] == pivot):
                    junk = 1
                    self.comparisons+=2
                else:
                    higher.append(list[i])
                    self.comparisons+=3
            pivotList = [pivot]
            self.nums = lower + pivotList + higher
            import display
            display.updateAlgo(self)
            return self.sort(lower) + pivotList + self.sort(higher)
        else:
            return list

    def sort(self, array=[], start=0, end=0):
        if array == []:
            array = self.nums
            end = len(array) - 1
        if start < end:
            pivot = self.partition(array,start,end)
            self.sort(array,start,pivot-1)
            self.sort(array,pivot+1,end)

    def partition(self, array, start, end):
        x = array[end]
        i = start-1
        for j in range(start, end+1, 1):
            if array[j] <= x:
                i += 1
                if i < j:
                    temp = self.nums[j]
                    self.nums[j] = self.nums[i]
                    self.nums[i] = temp
                    import display
                    display.updateAlgo(self)
        return i














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