# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = deque()
        if root:
            q.append(root)
        res = []
        while q:
            curr_sum = 0
            curr_amt = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                curr_amt += 1
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            res.append(curr_sum / curr_amt)
        return res
