class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        value = set()
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] in value:
                return i // 3 + 1
            value.add(nums[i])
        
        return 0
