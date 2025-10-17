class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        memo = {}

        def dp(mask, change, i):
            if (mask, change, i) in memo:
                return memo[(mask, change, i)]

            if i == len(s):
                return 1

            best = 0

            # continue with curr char
            curr = ord(s[i]) - ord('a')
            nmask = mask | (1 << curr)
            if nmask.bit_count() <= k:
                best = max(best, dp(nmask, change, i + 1))
            else:
                best = max(best, dp(1 << curr, change, i + 1) + 1)

            # try new chars
            if not change:
                for j in range(26):
                    if j == curr:
                        continue
                    nmask = mask | (1 << j)
                    if nmask.bit_count() <= k:
                        best = max(best, dp(nmask, True, i + 1))
                    else:
                        best = max(best, dp(1 << j, True, i + 1) + 1)

            memo[(mask, change, i)] = best
            return best

        return dp(0, False, 0)