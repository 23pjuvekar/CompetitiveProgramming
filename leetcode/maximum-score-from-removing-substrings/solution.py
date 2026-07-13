class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def helper(s, first, second, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)

            return "".join(stack), score

        if x > y:
            s, score1 = helper(s, 'a', 'b', x)
            s, score2 = helper(s, 'b', 'a', y)
        else:
            s, score2 = helper(s, 'b', 'a', y)
            s, score1 = helper(s, 'a', 'b', x)

        return score1 + score2
