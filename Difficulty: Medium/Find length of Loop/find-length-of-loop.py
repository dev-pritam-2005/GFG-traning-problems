'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        # code here
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                count = 1
                fast = fast.next

                while slow != fast:
                    count += 1
                    fast = fast.next

                return count

        return 0
        