class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:

        res = 0
        visited = set()

        for num in nums:
            if num in visited:
                res = res ^ num
            else:
                visited.add(num)
        return res
