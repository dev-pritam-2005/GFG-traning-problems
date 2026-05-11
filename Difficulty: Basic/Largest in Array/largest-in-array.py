class Solution:
    def largest(self, arr):
        max1 = arr[0]
        for it in arr:
            if it > max1:
                max1 = it 
        return max1
