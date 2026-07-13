class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            gd = nums[i]
            for j in range(i, n):
                gd = gcd(gd, nums[j])
                if gd == k:
                    cnt += 1
        return cnt
