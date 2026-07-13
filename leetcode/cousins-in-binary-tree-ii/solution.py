# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q = deque()
        if root:
            q.append([root, None])
        
        while q:
            new_q = deque()
            parent_sum = defaultdict(int)
            total = 0
            for i in range(len(q)):
                node, parent = q[i]
                parent_sum[parent] += node.val
                total += node.val
                if node.right:
                    new_q.append([node.right, node])
                if node.left:
                    new_q.append([node.left, node])
            for i in range(len(q)):
                node, parent = q[i]
                node.val = total - parent_sum[parent]
            q = new_q
        return root
