# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        hashmap = set()
        def recurse_get(node):
            if not node:
                return
            hashmap.add(target - node.val)
            recurse_get(node.left)
            recurse_get(node.right)
        def recurse_find(node):
            if not node:
                return False
            if node.val in hashmap:
                return True
            return recurse_find(node.left) or recurse_find(node.right)
        recurse_get(root1)
        return recurse_find(root2)
