class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:

        left = 0
        ans = 0
        cnt = defaultdict(int)
        for x in s:
            cnt[x] += 1
            while cnt[x] >= k:
                cnt[s[left]] -= 1
                if (cnt[s[left]] == 0):
                    cnt.pop(s[left])
                left += 1
            ans += left
        return ans
