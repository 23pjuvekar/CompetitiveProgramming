class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        
        count = defaultdict(int)
        res = [0] * (len(nums) - k + 1)

        for i in range(len(nums)):
            if nums[i] < 0:
                count[nums[i]] += 1
            if i - k >= 0 and nums[i - k] < 0:
                count[nums[i-k]] -= 1
            if i - k + 1 < 0:
                continue
            c = 0
            for j in range(-50, 0):
                c += count[j]
                if c >= x:
                    res[i - k + 1] = j
                    break
        return res
