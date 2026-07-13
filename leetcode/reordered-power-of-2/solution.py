class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        values = defaultdict(list)
        for i in range(30):
            values[len(str(2**i))].append(str(2**i))

        length = len(str(n))
        for possible in values[length]:
            if Counter(str(n)) == Counter(possible):
                return True
        return False
