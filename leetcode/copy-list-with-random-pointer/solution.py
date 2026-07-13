"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        oldToNew = { None : None }

        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            temp = oldToNew[curr]
            temp.next = oldToNew[curr.next]
            temp.random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]
