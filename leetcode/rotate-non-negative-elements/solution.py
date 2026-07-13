class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:

        n_i = []
        n = []

        for i in range(len(nums)):
            if nums[i] >= 0:
                n.append(nums[i])
                n_i.append(i)
        if not n:
            return nums
        k = k % len(n)
        n = n[k:] + n[:k]
        for i, num in zip(n_i, n):
            nums[i] = num
        return nums
