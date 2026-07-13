class Solution:

    def __init__(self, w: List[int]):
        self.stack = [w[0]]
    
        for val in w[1:]:
            self.stack.append(val+self.stack[-1])
        

    def pickIndex(self) -> int:
        num = random.randint(1, self.stack[-1])
        return bisect.bisect_left(self.stack, num)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
