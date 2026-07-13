class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        res = nums.sort()
        res = []


        l = 0
        r = len(nums) - 1

        while l < r:
            res.append(nums[l])
            res.append(nums[r])
            l += 1
            r -= 1

        if l == r:
            res.append(nums[l])

        for i in range(len(res)):
            nums[i] = res[i]
