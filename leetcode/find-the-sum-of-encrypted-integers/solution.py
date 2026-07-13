class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            max_val = 0
            for c in str(num):
                val = int(c)
                max_val = max(max_val, val)
            res += int("".join([str(max_val)] * len(str(num))))
        return res
