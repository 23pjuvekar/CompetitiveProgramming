class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:

        cnt = defaultdict(int)
        ma = 0
        res = ""
        for m, s in zip(messages, senders):
            cnt[s] += len(m.split(" "))
            if cnt[s] > ma:
                res = s
                ma = cnt[s]
            elif cnt[s] == ma:
                res = max(res, s)
        return res
