class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        if not root:
            return 0
        
        def dfs(node=root):
            if node is None:
                return (0, 0)
            
            sum_left, node_cnt_left = dfs(node.left)
            sum_right, node_cnt_right = dfs(node.right)
            _total_sum = node.val + sum_left + sum_right
            _total_nodes = 1 + node_cnt_left + node_cnt_right
            _avg = _total_sum / _total_nodes
            
            if _avg > self.max_avg:
                self.max_avg = _avg
            
            return (_total_sum, _total_nodes)
        
        self.max_avg = float("-inf")
        dfs()

        return self.max_avg
