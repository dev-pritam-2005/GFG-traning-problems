class Solution:
    def prevSmaller(self, arr):
        stack = []
        ans = []

        for num in arr:

            
            while stack and stack[-1] >= num:
                stack.pop()

            
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])


            stack.append(num)

        return ans