# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        q = deque()
        res = 0
        if root:
            q.append([root, 0])
        while q:
            for _ in range(len(q)):
                node, val = q.popleft()
                if node.right:
                    q.append([node.right, 2 * val + node.val])
                if node.left:
                    q.append([node.left, 2 * val + node.val])
                if not node.right and not node.left:
                    res += 2 * val + node.val
            print(res)
        return res
