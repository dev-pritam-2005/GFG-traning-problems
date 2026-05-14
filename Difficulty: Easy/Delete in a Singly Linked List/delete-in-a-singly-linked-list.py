'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        if(x == 1):
            temp = head
            head = head.next
            temp.next = None
        else:
            prev = head
            for x in range(x-2):
                prev = prev.next
        
            temp = prev.next
            prev.next = temp.next
            temp.next = None
        
        return head