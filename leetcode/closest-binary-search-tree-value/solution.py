# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        closest = float("inf")

        while root:
            if abs(target - closest) > abs(target - root.val):
                closest = root.val
            elif abs(target - closest) == abs(target - root.val):
                closest = min(closest, root.val)

            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                return int(target)
            
        return closest
