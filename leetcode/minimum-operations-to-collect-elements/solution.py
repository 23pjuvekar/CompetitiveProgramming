class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        values = set()
        cnt = 0
        for i in range(len(nums) - 1, -1, -1):
            cnt += 1
            if 1 <= nums[i] <= k:
                values.add(nums[i])
            if len(values) == k:
                return cnt
