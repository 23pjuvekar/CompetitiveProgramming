class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:

        freq = Counter(nums)

        options = list(set(nums))
        options.sort()
        previous_freq = freq[options[0]]
        for num in options:
            if freq[num] == previous_freq:
                continue
            else:
                return [options[0], num]
        return [-1, -1]
