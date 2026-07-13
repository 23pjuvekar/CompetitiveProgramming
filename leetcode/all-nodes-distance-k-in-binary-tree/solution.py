# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        res = []
        parent_list = {}
        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    parent_list[node.left.val] = node
                    q.append(node.left)
                
                if node.right:
                    parent_list[node.right.val] = node
                    q.append(node.right)

        visited = {}
        q.append(target)

        while k > 0 and q:
            for i in range(len(q)):
                node = q.popleft()

                visited[node.val] = 1

                if node.left and node.left.val not in visited:
                    q.append(node.left)
                
                if node.right and node.right.val not in visited:
                    q.append(node.right)
                
                if node.val in parent_list and parent_list[node.val].val not in visited:
                    q.append(parent_list[node.val])
                
            k -= 1
        
        while q:
            res.append(q.popleft().val)
        
        return res
