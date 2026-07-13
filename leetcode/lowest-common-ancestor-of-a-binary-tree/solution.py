# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(curr_path, curr_node, target_node):
            if not curr_node: 
                return None
            current_path_for_node = curr_path + [curr_node]
            if curr_node == target_node:
                return current_path_for_node
            if curr_node.left:
                left_result = dfs(current_path_for_node, curr_node.left, target_node)
                if left_result:
                    return left_result
            if curr_node.right:
                right_result = dfs(current_path_for_node, curr_node.right, target_node)
                if right_result:
                    return right_result
            return None

        p_list = dfs([], root, p)
        q_list = dfs([], root, q)
        res = root
        for x, y in zip(p_list, q_list):
            if x != y:
                return res
            res = x
        return res
