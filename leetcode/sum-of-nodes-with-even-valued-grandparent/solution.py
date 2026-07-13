# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        q = deque()
        q.append([-1, -1, root])
        res = 0
        while q:
            for i in range(len(q)):
                grandparent, parent, node = q.popleft()
                if grandparent == 0:
                    res += node.val
                if node.left:
                    q.append([parent, node.val % 2, node.left])
                if node.right:
                    q.append([parent, node.val % 2, node.right])
        return res
