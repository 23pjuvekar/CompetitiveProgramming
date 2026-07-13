# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        while q:
            level_size = len(q)
            nodes = []
            for _ in range(level_size):
                node = q.popleft()
                nodes.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level % 2 == 1:
                left = 0
                right = len(nodes) - 1
                while left < right:
                    nodes[left].val, nodes[right].val = nodes[right].val, nodes[left].val
                    left += 1
                    right -= 1
            
            level += 1
            
        return root
