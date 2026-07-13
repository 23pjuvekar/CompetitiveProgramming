class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            copy_arr = nums[:i] + nums[i+1:]
            good = True
            for j in range(len(copy_arr) - 1):
                if copy_arr[j] >= copy_arr[j + 1]:
                    good = False
                    break
            if good:
                return good
        return False
