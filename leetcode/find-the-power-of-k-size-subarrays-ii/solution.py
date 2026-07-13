class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = []
        consecutive = 1

        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                consecutive += 1
            else:
                consecutive = 1

            if i >= k - 1:
                if consecutive >= k:
                    results.append(nums[i])
                else:
                    results.append(-1)

        if k == 1:
            return nums[:]

        return results
