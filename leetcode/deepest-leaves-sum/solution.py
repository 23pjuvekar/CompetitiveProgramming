# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        q = deque()
        if root:
            q.append(root)
        
        while q:
            res = 0
            for i in range(len(q)):
                node = q.popleft()
                res += node.val
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return res
