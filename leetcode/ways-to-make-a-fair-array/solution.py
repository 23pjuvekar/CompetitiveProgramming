class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        evensum = 0
        oddsum = 0

        for i in range(n):
            if i % 2 == 0:
                evensum += nums[i]
            else:
                oddsum += nums[i]

        lefteven = 0
        leftodd = 0
        ans = 0

        for i in range(n):
            if i % 2 == 0:
                evensum -= nums[i]
            else:
                oddsum -= nums[i]

            neweven = lefteven + oddsum
            newodd = leftodd + evensum

            if neweven == newodd:
                ans += 1

            if i % 2 == 0:
                lefteven += nums[i]
            else:
                leftodd += nums[i]

        return ans
