class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        res = []
        heapify(nums)

        while nums:
            v1 = heappop(nums)
            v2 = heappop(nums)
            res.append(v2)
            res.append(v1)
        return res
