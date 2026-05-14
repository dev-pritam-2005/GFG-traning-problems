class Solution:
    def preGreaterEle(self, arr):

        stack = []
        ans = []

        for num in arr:

            # Remove smaller or equal elements
            while stack and stack[-1] <= num:
                stack.pop()

            # Previous greater element
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])

            # Push current element
            stack.append(num)

        return ans