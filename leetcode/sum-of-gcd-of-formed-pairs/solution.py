class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        curr_max = nums[0]
        for num in nums:
            curr_max = max(curr_max, num)
            prefixGcd.append(math.gcd(num, curr_max))
        prefixGcd.sort()
        l = 0
        r = len(prefixGcd) - 1
        res = 0
        while l < r:
            res += math.gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1
        return res
