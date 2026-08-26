class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        

            prefix_sum = 0
            maxLen = 0

            # Stores first occurrence of prefix sum
            mp = {}

            for i in range(len(arr)):
                prefix_sum += arr[i]

                # If entire subarray from 0 to i has sum k
                if prefix_sum == k:
                    maxLen = i + 1

                # Check if there is an earlier prefix sum
                if prefix_sum - k in mp:
                    length = i - mp[prefix_sum - k]
                    maxLen = max(maxLen, length)

                # Store only first occurrence
                if prefix_sum not in mp:
                    mp[prefix_sum] = i

            return maxLen
        
        
        # this is optimal solution for only posetive number
        # n = len(arr)
        # maxLen = 0
        
        # right = 0
        # left=0
        # sum = arr[0]

        # while right<n:
            
            
        #     while left<=right and sum > k:
        #         sum -= arr[left]
        #         left+= 1
                
        #     if sum == k:
        #         maxLen = max(maxLen, right-left+1)
            
        #     right+=1
        #     if right<n:
        #         sum += arr[right]
        
        # return maxLen
        
        
        
        
        
        
        
        
        # brute force but just modified to o(n2)
        # n = len(arr)
        # maxlen = 0

        # for i in range(n):
        #     s = 0
        #     for j in range(i, n):
        #         s+=arr[j]
        #         if s == k:
        #             maxlen = max(maxlen, j - i + 1)

        # return maxlen  
        
        
        
        
        
        
        
        
        
        
        # brute  force but o(n 3)
        # n = len(arr)
        # maxlen = 0

        # for i in range(n):
        #     for j in range(i, n):
        #         s = 0
        #         for p in range(i, j + 1):   
        #             s += arr[p]
        #         if s == k:
        #             maxlen = max(maxlen, j - i + 1)

        # return maxlen  
