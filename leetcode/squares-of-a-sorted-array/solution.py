class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        first_pos = len(nums)
        res = []
        
        for index, val in enumerate(nums):
            if val >= 0:
                first_pos = index
                break

        negative = first_pos - 1
        positive = first_pos

        while positive != len(nums) or negative != -1:
            if negative != -1 and positive != len(nums):
                if -nums[negative] < nums[positive]:
                    res.append(nums[negative] * nums[negative])
                    negative -= 1
                else:
                    res.append(nums[positive] * nums[positive])
                    positive += 1
            elif negative != -1:
                res.append(nums[negative] * nums[negative])
                negative -= 1
            else:
                res.append(nums[positive] * nums[positive])
                positive += 1

        return res
