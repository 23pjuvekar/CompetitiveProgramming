class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        best_split: List[int] | None = None
        best_diff = float("inf")

        def dfs(level: int, start: int, remaining: int, path: List[int]) -> None:
            nonlocal best_split, best_diff

            if level == k - 1:
                last = remaining
                if last >= start:
                    candidate = path + [last]
                    diff = max(candidate) - min(candidate)
                    if diff < best_diff:
                        best_diff = diff
                        best_split = candidate
                return

            i = start
            while i * i <= remaining:
                if remaining % i == 0:
                    dfs(level + 1, i, remaining // i, path + [i])
                i += 1

        dfs(0, 1, n, [])

        if best_split is None:
            best_split = [1] * (k - 1) + [n]

        return best_split
