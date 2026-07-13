class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def bt(start, seen):
            if start == len(s):
                return 0
            max_splits = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in seen:
                    seen.add(substring)
                    max_splits = max(max_splits, 1 + bt(end, seen))
                    seen.remove(substring)
            return max_splits
        return bt(0, set())
