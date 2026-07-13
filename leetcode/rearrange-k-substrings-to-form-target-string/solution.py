class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:

        n = len(s)
        jump = n // k
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)
        for i in range(0, n, jump):
            s_freq[s[i:i+jump]] += 1
            t_freq[t[i:i+jump]] += 1
        return s_freq == t_freq
