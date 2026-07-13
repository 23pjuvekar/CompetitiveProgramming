class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append([s[i], goal[i]])
                if len(diff) == 3:
                    return False
        if len(diff) == 0:
            return max(Counter(s).values()) > 1
        if len(diff) != 2:
            return False
        
        return diff[0][0] == diff[1][1] and diff[1][0] == diff[0][1]
