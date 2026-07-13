class Solution:
    def minOperations(self, logs: List[str]) -> int:

        level = 0


        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                level = max(0, level - 1)
            else:
                level += 1
        return level
