class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        res = []
        for l_i, r_i in zip(l, r):
            if r_i == l_i:
                res.append(False)
            else:
                good = True
                difference = nums[l_i + 1] - nums[l_i]
                min_value = min(nums[l_i:r_i+1])
                max_value = max(nums[l_i:r_i+1])
                n = len(nums[l_i:r_i+1])
                if (max_value - min_value) % (n - 1) != 0:
                    res.append(False)
                    continue
                difference = (max_value - min_value) // (n - 1)
                if difference == 0:
                    res.append(True)
                    continue
                values_set = set(nums[l_i:r_i+1])
                for value in range(min_value, max_value + 1, difference):
                    if value not in values_set:
                        good = False
                        break
                res.append(good)
        return res
