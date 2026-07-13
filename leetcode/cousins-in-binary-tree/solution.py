# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        q = deque()
        x_f = []
        y_f = []
        if root:
            q.append([root, None])
        while q:
            for i in range(len(q)):
                node, parent = q.popleft()
                if node.val == x:
                    x_f = [node, parent]
                if node.val == y:
                    y_f = [node, parent]
                if node.right:
                    q.append([node.right, node])
                if node.left:
                    q.append([node.left, node])
            if len(x_f) == 2 and len(y_f) == 2:
                return x_f[1] != y_f[1]
            elif len(x_f) == 2 or len(y_f) == 2:
                return False
        return False
