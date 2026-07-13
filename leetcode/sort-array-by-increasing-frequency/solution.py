class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        r = Counter(nums).most_common()
        r.sort(key = lambda x: (x[1], -x[0]))

        res = []
        for i in r:
            a, b = i
            res.extend([a]*b)
            
        return res
