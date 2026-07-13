class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        A = sum(aliceSizes)
        B = sum(bobSizes)
        B_set = set(bobSizes)
        diff = (A - B) // 2
        for a in aliceSizes:
            if a - diff in B_set:
                return [a, a - diff]
