class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        balanced_pairs = min(x, y)

        if x == y:
            aa_bb_length = 4 * balanced_pairs
        else:
            aa_bb_length = balanced_pairs * 4 + 2

        ab_length = 2 * z

        return aa_bb_length + ab_length
