class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        
        res = 0
        m = len(str(nums[0]))
        n = len(nums)
        c1 = [ [0] * 10 for _ in range(m)]
        for num in nums:
            i = 0
            while num:
                c1[i][num % 10] += 1
                num = num // 10
                i += 1
        print(c1)
        for i in range(m):
            for j in range(10):
                res += (c1[i][j]) * (n- (c1[i][j]))
        return res // 2
