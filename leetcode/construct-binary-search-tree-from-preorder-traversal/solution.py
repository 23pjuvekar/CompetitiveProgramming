class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(lower, upper):
            nonlocal idx

            if idx == n:
                return None
            
            val = preorder[idx]
            
            if val < lower or val > upper:
                root = None
                return None
            
            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root
        
        idx = 0
        n = len(preorder)
        return helper(float("-inf"), float("inf"))
