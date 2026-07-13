class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = ""
        q = deque()
        q.append([root, chr(root.val + ord('a'))])
        while q:
            node, curr_string = q.popleft()
            if not node.left and not node.right:
                res = min(res, curr_string) if res else curr_string
            
            if node.left:
                q.append([node.left, chr(node.left.val + ord('a')) + curr_string])
            
            if node.right:
                q.append([node.right, chr(node.right.val + ord('a')) + curr_string])

        return res
