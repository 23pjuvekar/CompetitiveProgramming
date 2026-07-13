class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = set()
        for i in range(n):
            if key == nums[i]:
                for j in range(max(0, i - k), min(n, i + k + 1)):
                    res.add(j)
        return list(res)
