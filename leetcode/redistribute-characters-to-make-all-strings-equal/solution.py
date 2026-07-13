class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        c1 = defaultdict(int)

        for word in words:
            for c in word:
                c1[c] += 1
        
        n = len(words)

        for key, val in c1.items():
            if val % n != 0:
                return False
        return True
