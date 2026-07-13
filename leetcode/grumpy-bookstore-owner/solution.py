class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        total_happy = 0
        for g, c in zip(grumpy, customers):
            if g == 0:
                total_happy += c

        curr_grumpy = 0
        l = 0
        res = 0
        for r in range(len(customers)):
            if grumpy[r] == 1:
                curr_grumpy += customers[r]
            if r - l + 1 > minutes:
                if grumpy[l] == 1:
                    curr_grumpy -= customers[l]
                l += 1
            res = max(res, total_happy + curr_grumpy)
        return res
