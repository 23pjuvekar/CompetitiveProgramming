class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        xor = [nums[0]]
        for i in range(1, len(nums)):
            xor.append(xor[-1] ^ nums[i])
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append((2 ** maximumBit - 1) ^ xor[i])
        return res
