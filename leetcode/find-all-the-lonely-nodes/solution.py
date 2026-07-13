# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:

        q = deque()
        res = []
        if root:
            q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.right and node.left:
                    q.append(node.right)
                    q.append(node.left)
                elif node.right:
                    q.append(node.right)
                    res.append(node.right.val)
                elif node.left:
                    q.append(node.left)
                    res.append(node.left.val)
        return res
