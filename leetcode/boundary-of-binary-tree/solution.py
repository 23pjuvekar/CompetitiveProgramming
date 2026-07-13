class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        def leftdfs(node):
            if node:
                if node.left is None and node.right is None:
                    return []
                else:
                    if node.left:
                        return [node.val] + leftdfs(node.left)
                    else:
                        return [node.val] + leftdfs(node.right)
            else:
                return []
        
        def findLeaves(node):
            if node:
                if node.right is None and node.left is None:
                    return [node.val]
                else:
                    return findLeaves(node.left) + findLeaves(node.right)
            else:
                return []
        
        def rightdfs(node):
            if node:
                if node.left is None and node.right is None:
                    return []
                else:
                    if node.right:
                        return rightdfs(node.right) + [node.val]
                    else:
                        return rightdfs(node.left) + [node.val]
            else:
                return []
    
        if not root.left and not root.right:
            return [root.val]
            
        leftandleavesandright = [root.val] + leftdfs(root.left) + findLeaves(root) + rightdfs(root.right)
        
        return(leftandleavesandright)
