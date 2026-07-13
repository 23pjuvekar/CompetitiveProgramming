class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:

        res = [] # (slope, l, r)
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 0:
                slope = 0
            else:
                slope = (nums[i + 1] - nums[i]) // abs(nums[i + 1] - nums[i])
            if res and res[-1][0] == slope:
                res[-1][2] = i + 1
            else:
                res.append([slope, i, i + 1])
        prefix = [0]
        curr = 0
        for num in nums:
            curr += num
            prefix.append(curr)
        pos = []
        final_r = float("-inf")
        for i in range(len(res) - 2):
            if res[i][0] == 1 and res[i + 1][0] == -1 and res[i + 2][0] == 1:
                pos.append((res[i][1], res[i + 2][2]))
                r = res[i + 2][2]
                r_b = res[i + 2][1]
                while r != r_b + 1 and nums[r] < 0:
                    r -= 1
                l = res[i][1]
                l_b = res[i][2]
                while l != l_b - 1 and nums[l] < 0:
                    l += 1
                final_r = max(prefix[r + 1] - prefix[l], final_r)
                final_r = max(prefix[r_b + 2] - prefix[l], final_r)
        if final_r == float("-inf"):
            return -1
        return final_r
