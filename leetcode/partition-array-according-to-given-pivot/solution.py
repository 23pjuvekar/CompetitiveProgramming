class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        prev = []
        mid = []
        end = []

        for num in nums:
            if num < pivot:
                prev.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                end.append(num)
            
        return prev + mid + end


        """
        i, j = 0, len(nums) - 1
        i2, j2 = 0, len(nums) - 1
        res = [pivot] * len(nums)
        while i < len(nums):
            if nums[i] < pivot:
                res[i2] = nums[i]
                i2 += 1
            if nums[j] > pivot:
                res[j2] = nums[j]
                j2 -= 1
            i += 1
            j -= 1
        return res
        """
