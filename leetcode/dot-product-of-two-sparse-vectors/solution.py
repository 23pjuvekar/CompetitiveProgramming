class SparseVector:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.vector = defaultdict()
        for i in range(len(nums)):
            if nums[i] != 0:
                self.vector[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in range(self.n):
            if i not in self.vector or i not in vec.vector:
                continue
            res += self.vector[i] * vec.vector[i]
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
