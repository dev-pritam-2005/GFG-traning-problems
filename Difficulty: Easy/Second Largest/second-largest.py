class Solution:
    def getSecondLargest(self, arr):
        maxVal = -1
        secondMax = -1

        for num in arr:
            if num > maxVal:
                secondMax = maxVal
                maxVal = num
            elif num > secondMax and num != maxVal:
                secondMax = num

        return secondMax