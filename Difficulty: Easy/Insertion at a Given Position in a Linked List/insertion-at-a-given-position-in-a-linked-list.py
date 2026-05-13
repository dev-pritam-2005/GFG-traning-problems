'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def insertPos(self, head, pos, val):

        newNode = Node(val)

       
        if pos == 1:
            newNode.next = head
            return newNode

        curr = head
        count = 1

        
        while curr is not None and count < pos - 1:
            curr = curr.next
            count += 1


      
        newNode.next = curr.next
        curr.next = newNode

        return head