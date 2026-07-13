# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        q = deque()
        if original:
            q.append([original, cloned])
        while q:
            for _ in range(len(q)):
                node1, node2 = q.popleft()
                if node1 == target:
                    return node2
                if node1.left:
                    q.append([node1.left, node2.left])
                if node1.right:
                    q.append([node1.right, node2.right])
