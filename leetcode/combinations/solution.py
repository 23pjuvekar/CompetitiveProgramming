class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(current_combination, start_num):
            if len(current_combination) == k:
                result.append(list(current_combination))
                return
            if n - start_num + 1 < k - len(current_combination):
                return
            for num in range(start_num, n + 1):
                current_combination.append(num)
                backtrack(current_combination, num + 1)
                current_combination.pop()
        backtrack([], 1)
        return result
