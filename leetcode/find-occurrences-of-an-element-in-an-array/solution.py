class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:

        seens = []

        for i in range(len(nums)):
            if nums[i] == x:
                seens.append(i)
        
        res = []
        n = len(seens)
        for q in queries:
            if q > n:
                res.append(-1)
            else:
                res.append(seens[q-1])
        return res
