class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:

        # optimal
        numbers = Counter(nums)
        nums = list(set(nums))
        nums.sort()
        current_minimum = float("-inf")
        res = 0

        for num in nums:
            count = numbers[num]
            minimum = max(num - k, current_minimum)
            maximum = num + k
            coverage = min(maximum - minimum + 1, count)
            res += max(0, coverage)
            current_minimum = minimum + coverage
        return res

        
        # brute force
        res = set()
        nums.sort()
        for num in nums:
            for i in range(-k, k + 1, 1):
                if num + i not in res:
                    res.add(num + i)
                    break
        return len(res)