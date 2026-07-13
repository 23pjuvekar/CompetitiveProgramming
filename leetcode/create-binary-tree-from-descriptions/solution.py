# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        value_to_nodes = {}
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in value_to_nodes:
                value_to_nodes[parent] = TreeNode(parent)
            parent_node = value_to_nodes[parent]
            
            if child not in value_to_nodes:
                value_to_nodes[child] = TreeNode(child)
            child_node = value_to_nodes[child]
            
            if isLeft:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            children.add(child)

        for val in value_to_nodes:
            if val not in children:
                return value_to_nodes[val]
