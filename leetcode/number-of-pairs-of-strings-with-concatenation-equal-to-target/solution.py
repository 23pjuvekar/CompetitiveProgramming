class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:

        c1 = Counter(nums)
        n = len(target)
        res = 0
        for num in nums:
            c1[num] -= 1
            start = target[:n - len(num)]
            end = target[len(num):]
            if num + end == target:
                res += c1[end]
            if start + num == target:
                res += c1[start]
        return res
