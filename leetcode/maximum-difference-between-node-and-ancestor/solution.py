# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        q = deque()
        q.append([root, float("-inf"), float("inf")])
        res = 0
        while q:
            node, max_ancestor, min_ancestor = q.popleft()
            # print(node.val, max_ancestor, min_ancestor)
            if max_ancestor != float("inf"):
                res = max(max_ancestor - node.val, res)
            if min_ancestor != float("-inf"):
                res = max(node.val - min_ancestor, res)
            if node.right:
                q.append([node.right, max(max_ancestor, node.val), min(min_ancestor, node.val)])
            if node.left:
                q.append([node.left, max(max_ancestor, node.val), min(min_ancestor, node.val)])
        return res
