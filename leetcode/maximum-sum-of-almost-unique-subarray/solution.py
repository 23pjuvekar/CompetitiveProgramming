class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:

        n = len(nums)
        max_sum = 0
        window_sum = 0
        freq = defaultdict(int)
        for i in range(k):
            window_sum += nums[i]
            freq[nums[i]] += 1
            
        if len(freq) >= m:
            max_sum = window_sum
            
        for i in range(k, n):
            out_elem = nums[i - k]
            in_elem = nums[i]
            
            window_sum = window_sum - out_elem + in_elem
            
            freq[out_elem] -= 1
            if freq[out_elem] == 0:
                del freq[out_elem]
            
            freq[in_elem] += 1
            
            if len(freq) >= m:
                max_sum = max(max_sum, window_sum)
                
        return max_sum
