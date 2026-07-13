class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        counter = Counter(nums)
        def bt(temp):
            if len(temp) == len(nums):
                res.append(temp)
                return
            
            for key in counter:
                if counter[key] != 0:
                    counter[key] -= 1
                    bt(temp + [key])
                    counter[key] += 1
        bt([])
        return res
