class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        length = len(tops)

        freq_top = Counter(tops)
        freq_bottom = Counter(bottoms)

        swap_number = None

        for i in range(1, 7):
            if freq_top[i] + freq_bottom[i] >= length:
                swap_number = i
                break
        
        for i in range(length):
            if swap_number not in [tops[i], bottoms[i]]:
                return -1
        
        min_1 = length - freq_top[swap_number]
        min_2 = length - freq_bottom[swap_number]

        return min(min_1, min_2)
