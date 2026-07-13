class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        previous_sequence = self.countAndSay(n - 1)
        result = []
        count = 1
        for i in range(1, len(previous_sequence)):
            if previous_sequence[i] == previous_sequence[i - 1]:
                count += 1
            else:
                result.append(str(count))
                result.append(previous_sequence[i - 1])
                count = 1
        result.append(str(count))
        result.append(previous_sequence[-1])

        return "".join(result)
