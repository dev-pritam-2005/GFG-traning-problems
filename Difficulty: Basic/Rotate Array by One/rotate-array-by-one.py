class Solution:
    def rotate(self, arr):
        temp = arr[len(arr)-1]

        for k in range(len(arr)-1,0,-1):
            arr[k] = arr[k-1]
        arr[0] =  temp
    
