class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        if len(s) % 2 == 1:
            return False
        
        s_locked = []
        s_unlocked = []

        for i in range(len(s)):
            if locked[i] == "0":
                s_unlocked.append(i)
            elif s[i] == "(":
                s_locked.append(i)
            else:
                if s_locked:
                    s_locked.pop()
                elif s_unlocked:
                    s_unlocked.pop()
                else:
                    return False
        
        while s_locked and s_unlocked and s_locked[-1] < s_unlocked[-1]:
            s_locked.pop()
            s_unlocked.pop()
        
        return not s_locked
