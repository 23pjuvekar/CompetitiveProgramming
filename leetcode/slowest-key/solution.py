class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:

        res = "a"
        ma = 0
        prev = 0
        for time, key in zip(releaseTimes, keysPressed):
            total = time - prev
            if total > ma:
                res = key
                ma = total
            elif total == ma:
                res = max(key, res)
            prev = time
        return res
