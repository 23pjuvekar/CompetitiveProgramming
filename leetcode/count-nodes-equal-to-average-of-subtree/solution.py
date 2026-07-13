# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        self.res = 0

        def dfs(node):
            if not node:
                return 0, 0
            
            value_return = [node.val, 1]
            if node.left:
                left_return = dfs(node.left)
                value_return[0] += left_return[0]
                value_return[1] += left_return[1]
            if node.right:
                right_return = dfs(node.right)
                value_return[0] += right_return[0]
                value_return[1] += right_return[1]
            if value_return[0] // value_return[1] == node.val:
                self.res += 1
            return value_return

        dfs(root)
        return self.res
