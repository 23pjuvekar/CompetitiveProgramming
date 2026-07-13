class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:

        seen = []
        cnt = 0
        ans = []
        for c in nums:
            if c != -1:
                cnt = 0
                seen.append(c)
            else:
                cnt += 1
                if cnt - 1 < len(seen):
                    ans.append(seen[-cnt])
                else:
                    ans.append(-1)
        return ans
