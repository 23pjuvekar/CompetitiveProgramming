class Solution:
    def maxScore(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0] * nums[0]

        pref_gcd = [0] * n
        pref_lcm = [0] * n
        pref_gcd[0], pref_lcm[0] = nums[0], nums[0]
        for i in range(1, n):
            pref_gcd[i] = math.gcd(pref_gcd[i - 1], nums[i])
            pref_lcm[i] = math.lcm(pref_lcm[i - 1], nums[i])

        suff_gcd = [0] * n
        suff_lcm = [0] * n
        suff_gcd[-1], suff_lcm[-1] = nums[-1], nums[-1]
        
        for i in range(n - 2, -1, -1):
            suff_gcd[i] = math.gcd(suff_gcd[i + 1], nums[i])
            suff_lcm[i] = math.lcm(suff_lcm[i + 1], nums[i])

        max_val = pref_gcd[n - 1] * pref_lcm[n - 1]
        
        for i in range(n):
            if i == 0:
                score = suff_gcd[1] * suff_lcm[1]
            elif i == n - 1:
                score = pref_gcd[n - 2] * pref_lcm[n - 2]
            else:
                g = math.gcd(pref_gcd[i - 1], suff_gcd[i + 1])
                l = math.lcm(pref_lcm[i - 1], suff_lcm[i + 1])
                score = g * l
            
            max_val = max(max_val, score)
            
        return max_val
