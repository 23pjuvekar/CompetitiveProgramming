class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:

        count = Counter(nums)
        amt = defaultdict(int)
        for key, val in count.items():
            amt[val] += 1
        for num in nums:
            if amt[count[num]] == 1:
                return num
        return -1
