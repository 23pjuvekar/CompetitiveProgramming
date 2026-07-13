class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:

        post = Counter(nums)
        p_a = len(post)
        pre = set()
        p_b = 0
        n = len(nums)
        res = [0] * n
        for i in range(n):
            if nums[i] not in pre:
                pre.add(nums[i])
                p_b += 1
            post[nums[i]] -= 1
            if post[nums[i]] == 0:
                p_a -= 1
            res[i] = p_b - p_a
        return res
