class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        n = sum(chalk)
        k = k % n
        
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
