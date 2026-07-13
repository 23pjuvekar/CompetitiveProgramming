# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0


        res = 0
        q = deque()
        q.append([root, False])

        while q:
            for i in range(len(q)):
                node, good = q.popleft()
                if node.left:
                    q.append([node.left, True])
                if node.right:
                    q.append([node.right, False])
                if not node.left and not node.right and good:
                    res += node.val
        
        return res
