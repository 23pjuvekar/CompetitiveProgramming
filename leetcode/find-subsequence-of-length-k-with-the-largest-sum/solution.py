class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        num_and_index = [[nums[i], i] for i in range(len(nums))]
        num_and_index.sort(reverse=True)
        num_and_index = num_and_index[:k]
        num_and_index.sort(key=lambda x: x[1])
        res = [num for num, i in num_and_index]
        return res
