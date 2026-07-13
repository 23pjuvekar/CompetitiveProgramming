class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:

        c1 = defaultdict(int)
        m = 0
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] == key:
                c1[nums[i + 1]] += 1
                if c1[nums[i + 1]] > m:
                    m = c1[nums[i + 1]]
                    res = nums[i + 1]
        return res
