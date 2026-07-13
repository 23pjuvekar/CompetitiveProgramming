class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        current_sum = 0
        window = defaultdict(int)
        l = 0
        
        for r in range(len(nums)):
            window[nums[r]] += 1
            current_sum += nums[r]
            
            while window[nums[r]] > 1 or (r - l + 1) > k:
                window[nums[l]] -= 1
                current_sum -= nums[l]
                l += 1
            
            if r - l + 1 == k:
                res = max(res, current_sum)
                
        return res
