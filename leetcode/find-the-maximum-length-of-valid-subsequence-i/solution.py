class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        res = [0, 0, 0, 0]
        last = [0, 1, 0, 1]
        for num in nums:
            if num % 2 != last[0]:
                last[0] = num % 2
                res[0] += 1
            if num % 2 != last[1]:
                last[1] = num % 2
                res[1] += 1
            if num % 2 == last[2]:
                res[2] += 1
            else:
                res[3] += 1
        return max(res)
