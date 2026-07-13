class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:

        array_sort = []
        for num in nums:
            array_sort.append([int(str(int(bin(num)[2:]))[::-1]), num])
        array_sort.sort()
        res = []
        for _, num in array_sort:
            res.append(num)
        return res
