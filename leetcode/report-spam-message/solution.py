class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:

        b = set(bannedWords)
        res = 0

        for m in message:
            if m in b:
                res += 1
                if res > 1:
                    return True
        return res > 1
