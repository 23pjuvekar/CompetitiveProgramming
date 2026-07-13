class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        col_counts = []
        for j in range(n):
            column_data = [grid[i][j] for i in range(m)]
            col_counts.append(Counter(column_data))

        memo = {}

        def get_max_kept(col_idx, last_value):
            if col_idx == n:
                return 0
            state = (col_idx, last_value)
            if state in memo:
                return memo[state]

            max_cells = 0
            for current_val in range(10):
                if current_val != last_value:
                    kept = col_counts[col_idx].get(current_val, 0)
                    res = kept + get_max_kept(col_idx + 1, current_val)
                    max_cells = max(max_cells, res)
            memo[state] = max_cells
            return max_cells
        total_max_kept = get_max_kept(0, -1)
        return (m * n) - total_max_kept
