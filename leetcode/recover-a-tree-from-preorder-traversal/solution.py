# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        node_and_levels = deque()
        i = 0
        while i < len(traversal):
            curr_level = 0
            while i < len(traversal) and traversal[i] == "-":
                curr_level += 1
                i += 1
            node_val_str = ""
            while i < len(traversal) and traversal[i].isdigit():
                node_val_str += traversal[i]
                i += 1
            if node_val_str:
                node_and_levels.append([int(node_val_str), curr_level])

        if not node_and_levels:
            return None
        curr_path = []
        root = None
        node_val, level = node_and_levels.popleft()
        root = TreeNode(node_val)
        curr_path.append(root)
        while node_and_levels:
            node_val, level = node_and_levels.popleft()
            while len(curr_path) > level:
                curr_path.pop()
            parent_node = curr_path[-1] 
            new_node = TreeNode(node_val)
            if parent_node.left is None:
                parent_node.left = new_node
            else:
                parent_node.right = new_node
            curr_path.append(new_node)
        return root
