class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        counter = Counter(s)
        allowed = 0
        if len(s) % 2 == 1:
            allowed += 1

        for item in counter.items():
            if item[1] % 2 == 1:
                allowed -= 1
            if allowed == -1:
                return False
        return True
