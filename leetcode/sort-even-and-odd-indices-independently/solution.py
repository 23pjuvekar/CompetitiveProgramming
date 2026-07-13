class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        odd = []
        even = []

        for i in range(len(nums)):
            num = nums[i]
            if i % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        even.sort()
        odd.sort(reverse=True)

        e_i = 0
        o_i = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even[e_i]
                e_i += 1
            else:
                nums[i] = odd[o_i]
                o_i += 1
        return nums
