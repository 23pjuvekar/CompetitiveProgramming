class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        past_nums = defaultdict(list)
        res = float("inf")
        for i in range(len(nums)):
            past_nums[nums[i]].append(i)
            if len(past_nums[nums[i]]) > 2:
                res = min(res, abs(past_nums[nums[i]][-1] - past_nums[nums[i]][-2]) + abs(past_nums[nums[i]][-2] - past_nums[nums[i]][-3]) + abs(past_nums[nums[i]][-1] - past_nums[nums[i]][-3]))
        if res == float("inf"):
            return -1
        return res
