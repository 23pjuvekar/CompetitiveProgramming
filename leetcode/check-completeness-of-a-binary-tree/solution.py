# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        q = deque()
        curr = 1
        if root:
            q.append([root, 1])
        while q:
            node, n = q.popleft()
            if curr != n:
                return False
            if node.left:
                q.append([node.left, 2 * n])
            if node.right:
                q.append([node.right, 2 * n + 1])
            curr += 1
        return True
