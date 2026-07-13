class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        px = 0
        bal = 0
        ans = 0
        seen={(0,0):-1}
    
        for i, x in enumerate(nums):
            px^=x

            bal += 1 if x % 2 else -1

            key = (px,bal)

            if key in seen:
                ans = max(ans,i-seen[key])
            else:
                seen[key] = i
        return ans
