class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        
        q = [digit for digit in range(1, 10)]
        for _ in range(n - 1):
            q_next = []
            for num in q:
                t_digit = num % 10
                next_digits = set([t_digit + k, t_digit - k])

                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        q_next.append(new_num)
            q = q_next
        return q
