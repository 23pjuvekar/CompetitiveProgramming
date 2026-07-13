class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return nums
        
        n = len(nums)
        res = [-1] * (n - k + 1)
        l = 0
        last = float("-inf")
        for r in range(n):
            if last >= nums[r] or last + 1 != nums[r]:
                l = r
                last = nums[r]
                continue
            if r - l + 1 > k:
                l += 1    
            if r - l + 1 == k:
                res[l] = nums[r]
            last = nums[r]
        return res
