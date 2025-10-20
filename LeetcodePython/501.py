# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        node_counter = defaultdict(int)
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            node_counter[node.val] += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        curr_mode = 0
        curr_list = []
        for key, val in node_counter.items():
            if val > curr_mode:
                curr_list = [key]
                curr_mode = val
            elif val == curr_mode:
                curr_list.append(key)
        return curr_list
        