class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:

        result = []
        def backtrack(s, cost):
            if len(s) == n:
                result.append(s)
                return
            for c in "01":
                if c == "1":
                    if s and s[-1] == "1":
                        continue
                    new_cost = cost + len(s)
                    if new_cost > k:
                        continue
                    backtrack(s + c, new_cost)
                else:
                    backtrack(s + c, cost)
        backtrack("", 0)
        return result
