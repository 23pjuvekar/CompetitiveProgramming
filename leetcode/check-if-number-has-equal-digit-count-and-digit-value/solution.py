class Solution:
    def digitCount(self, num: str) -> bool:

        c1 = Counter(num)

        for i in range(len(num)):
            c = num[i]
            if int(c) != c1[str(i)]:
                return False
        return True
