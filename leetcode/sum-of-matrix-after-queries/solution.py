class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows_seen = set()
        cols_seen = set()
        total_sum = 0
        
        for i in range(len(queries) - 1, -1, -1):
            t, idx, val = queries[i]
            if t == 0:
                if idx not in rows_seen:
                    total_sum += val * (n - len(cols_seen))
                    rows_seen.add(idx)
            else:
                if idx not in cols_seen:
                    total_sum += val * (n - len(rows_seen))
                    cols_seen.add(idx)
                    
        return total_sum
