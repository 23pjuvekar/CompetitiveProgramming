class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        new_array = []
        for i in range(len(nums)):
            num = nums[i]
            new_num = ""
            for c in str(num):
                new_num += str(mapping[int(c)])
            new_num = int(new_num)
            new_array.append((new_num, i, num))
        new_array.sort()
        print(new_array)
        res = []
        for _, _, num in new_array:
            res.append(num)
        return res
