# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        even = True
        q = deque()
        if root:
            q.append(root)

        while q:
            prev = -1
            for _ in range(len(q)):
                node = q.popleft()
                if (even and node.val % 2 != 1) or (not even and node.val % 2 != 0):
                    return False
                if (prev != -1) and ((even and prev >= node.val) or (not even and prev <= node.val)):
                    return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev = node.val
            
            if even:
                even = False
            else:
                even = True
        return True
