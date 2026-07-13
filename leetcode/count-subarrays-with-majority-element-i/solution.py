class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        amt = [0]

        for num in nums:
            if num == target:
                amt.append(amt[-1] + 1)
            else:
                amt.append(amt[-1])
        # print(amt)
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                count = amt[j + 1] - amt[i]
                total_number = j - i + 1
                if total_number < count * 2:
                    res += 1
                    # print(i, j)
        return res
