class Solution:
    def findScore(self, nums: List[int]) -> int:

        marked = set()
        n = len(nums)
        h = []
        for i in range(len(nums)):
            h.append([nums[i], i])
        heapify(h)
        res = 0
        while n != len(marked):
            num, index = heappop(h)
            if index not in marked:
                res += num
                marked.add(index)
                if index - 1 > -1:
                    marked.add(index-1)
                if index + 1 < n:
                    marked.add(index+1)
        return res
