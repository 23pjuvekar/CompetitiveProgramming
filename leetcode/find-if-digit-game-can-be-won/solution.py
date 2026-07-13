class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        
        digit_2 = 0
        digit_1 = 0

        for n in nums:
            if n - 9 > 0: # 2 digit
                digit_2 += n
            else:
                digit_1 += n
        
        return not digit_1 == digit_2
