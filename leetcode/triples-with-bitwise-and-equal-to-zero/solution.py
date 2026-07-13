class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        
        two_pairs = defaultdict(int)
        for num1 in nums:
            for num2 in nums:
                two_pairs[num1 & num2] += 1
        res = 0
        for num3 in nums:
            mask = num3 ^ 0xffff
            curr = mask
            while curr:
                res += two_pairs[curr]
                curr = mask & (curr - 1)
            res += two_pairs[0]
        return res
