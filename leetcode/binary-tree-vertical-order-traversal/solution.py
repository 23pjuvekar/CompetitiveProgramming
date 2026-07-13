# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        q = deque()
        q.append([0, root])
        node_list = []
        node_list.append([0, root.val])
        max_neg = 0
        max_pos = 0

        while q:
            for i in range(len(q)):
                pos, node = q.popleft()
                if node.left:
                    max_neg = min(max_neg, pos - 1)
                    q.append([pos - 1, node.left])
                    node_list.append([pos - 1, node.left.val])
                if node.right:
                    max_pos = max(max_pos, pos + 1)
                    q.append([pos + 1, node.right])
                    node_list.append([pos + 1, node.right.val])


        print(max_neg)
        print(max_pos)
        print(node_list)

        res = []
        for i in range(max_pos - max_neg + 1):
            res.append([])
        for node in node_list:
            res[node[0] - max_neg].append(node[1])

        print(res)
        return res
