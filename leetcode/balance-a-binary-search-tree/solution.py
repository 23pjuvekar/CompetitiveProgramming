# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        values = []

        def getValues(curr):
            if not curr:
                return
            getValues(curr.left)
            values.append(curr.val)
            getValues(curr.right)
            
        def buildTree(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(values[mid])
            
            node.left = buildTree(left, mid - 1)
            node.right = buildTree(mid + 1, right)
            
            return node

        getValues(root)
        return buildTree(0, len(values) - 1)
