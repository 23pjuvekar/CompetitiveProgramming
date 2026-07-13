# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        if not root:
            return []
        
        stack = []
        res = []
        stack.append([root, str(root.val)])

        while stack:
            node, res_string = stack.pop()
            if not node.left and not node.right:
                res.append(res_string)
            if node.left:
                stack.append([node.left, res_string + "->" + str(node.left.val)])
            if node.right:
                stack.append([node.right, res_string + "->" + str(node.right.val)])
        
        return res
