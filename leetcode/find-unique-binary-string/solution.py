class Solution:
    def findDifferentBinaryString(self, nums):
        result = ""
        for i in range(len(nums)):
            current_char = nums[i][i]
            if current_char == '0':
                result += '1'
            else:
                result += '0'
        return result
