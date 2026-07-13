class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                n = min(len(numbers[i]), len(numbers[j]))
                if numbers[i][:n] == numbers[j][:n]:
                    return False
        return True
