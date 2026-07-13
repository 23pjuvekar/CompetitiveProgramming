class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total_even = 0
        for num in nums:
            if num % 2 == 0:
                total_even += num

        res = []
        for q in queries:
            old = nums[q[1]]
            nums[q[1]] += q[0]
            new = nums[q[1]]
            if (old % 2) != (new % 2):
                if (old % 2) == 0:
                    total_even -= old
                else:
                    total_even += new
            elif (new % 2) == 0:
                total_even += q[0]
            res.append(total_even)

        return res
