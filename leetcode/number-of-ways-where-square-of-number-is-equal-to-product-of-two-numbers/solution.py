class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count_triplets(a, b):
            freq = Counter(b)
            result = 0
            for x in a:
                sq = x * x
                for val, cnt in freq.items():
                    if sq % val == 0:
                        other = sq // val
                        if other == val:
                            result += cnt * (cnt - 1) // 2
                        elif other > val and other in freq:
                            result += cnt * freq[other]
            return result

        return count_triplets(nums1, nums2) + count_triplets(nums2, nums1)
