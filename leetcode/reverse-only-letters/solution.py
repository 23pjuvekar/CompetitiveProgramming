class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

        res = ""
        switch = len(s) - 1
        while switch > -1 and s[switch] not in letters:
            switch -= 1
        for i in range(len(s)):
            if s[i] not in letters:
                res += s[i]
            else:
                res += s[switch]
                switch -= 1
                while s[switch] not in letters:
                    switch -= 1
        return res
