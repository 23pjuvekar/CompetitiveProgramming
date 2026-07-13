class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        base = sum(1 for x in nums if x == k)
        distinct = set(nums)
        ans = base
        for v in distinct:
            if v == k:
                continue
            arr = []
            for x in nums:
                if x == v:
                    arr.append(1)
                elif x == k:
                    arr.append(-1)
                else:
                    arr.append(0)
            curr = 0
            mx = 0
            for val in arr:
                curr += val
                if curr > mx:
                    mx = curr
                if curr < 0:
                    curr = 0
            ans = max(ans, base + mx)
        return ans
