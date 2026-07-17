class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        shift_needed = [0] * len(s)
        usage_count = [0] * 26
        for index in range(len(s)):
            shift_needed[index] = (ord(t[index]) - ord(s[index]) + 26) % 26
        for index in range(len(s)):
            shift = shift_needed[index]
            if shift == 0:
                continue
            required_move = shift + usage_count[shift] * 26
            if required_move > k:
                return False
            usage_count[shift] += 1
        return True
