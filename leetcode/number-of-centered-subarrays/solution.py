class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for r in range(n):
            curr_sum = 0
            seen = set()
            for l in range(r, -1, -1):
                curr_sum += nums[l]
                seen.add(nums[l])

                if curr_sum in seen:
                    result += 1

        return result
