class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        def helper(node):
            if node:
                helper(node.right)
                self.total += node.val
                node.val = self.total
                helper(node.left)
        helper(root)
        return root
