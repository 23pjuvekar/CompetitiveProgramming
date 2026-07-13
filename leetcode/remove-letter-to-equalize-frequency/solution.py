class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        for key, value in sorted(counter.items()):
            counter[key]-=1
            amount = counter[key]
            if amount == 0:
                counter.pop(key)
            if len(set(counter.values())) == 1:
                return True
            if key not in counter:
                counter[key] = amount
            counter[key] += 1
        return False
