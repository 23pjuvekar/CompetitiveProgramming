class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        s1 = []
        if root1:
            s1.append(root1)
        r1 = []
        while s1:
            node = s1.pop()
            if node.right == None == node.left:
                r1.append(node.val)
            if node.right:
                s1.append(node.right)
            if node.left:
                s1.append(node.left)
        
        s2 = []
        if root2:
            s2.append(root2)
        r2 = []
        while s2:
            node = s2.pop()
            if node.right == None == node.left:
                r2.append(node.val)
            if node.right:
                s2.append(node.right)
            if node.left:
                s2.append(node.left)
        
        return r1 == r2
