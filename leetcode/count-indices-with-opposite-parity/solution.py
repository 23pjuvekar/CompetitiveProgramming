class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:

        answer = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] % 2 != nums[j] % 2:
                    answer[i] += 1
        return answer
