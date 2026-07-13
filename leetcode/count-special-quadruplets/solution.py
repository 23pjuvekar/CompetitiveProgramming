class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count_quad = 0
        ab_pairs = defaultdict(list)
        for idx_a in range(len(nums)-3):
            for idx_b in range(idx_a+1, len(nums)-2):
                pair_sum = nums[idx_a] + nums[idx_b]
                ab_pairs[pair_sum].append(idx_b)
        for idx_c in range(2, len(nums)-1):
            for idx_d in range(idx_c+1, len(nums)):
                pair_subtract = nums[idx_d] - nums[idx_c]
                if pair_subtract in ab_pairs.keys():
                    for idx_b in ab_pairs[pair_subtract]:
                        if idx_b < idx_c:
                            count_quad+=1
        return count_quad
