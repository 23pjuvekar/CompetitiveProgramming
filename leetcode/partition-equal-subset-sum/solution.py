class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target_2 = sum(nums)
        if target_2 % 2 == 1:
            return False

        dp = set()
        dp.add(0)
        target = target_2 // 2

        for i in range(len(nums)):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False
