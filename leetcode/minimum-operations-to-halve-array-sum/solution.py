class Solution:
    def halveArray(self, nums: List[int]) -> int:

        total = sum(nums)
        curr = total
        h = [-num for num in nums]
        heapify(h)
        res = 0
        while curr > total / 2:
            largest = -1 * heappop(h)
            curr -= largest
            curr += largest / 2
            heappush(h, - 1 * largest / 2)
            res += 1
        return res
