class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        # 1 --> possible
        # 2 --> not possible
        # 3 --> must be a multiple of length 3
        # 5 --> not possible
        # 7 --> 7, 14, 21, 28, 

        curr = 1
        for i in range(1, k + 1):
            curr = curr % k
            if curr == 0:
                return i
            curr = (10 * curr) + 1
        return -1

        # start: 1
        # (10 * start + 1) % 3 = 2
        # (10 * 2 + 1) % 3 = 0
        
        # 1 --> 1 (1)
        # 2 --> -1
        # 3 --> 3 (111)
        # 4 --> -1
        # 5 --> -1
        # 6 --> -1
        # 7 --> 6 (111111)
        # 8 --> -1
        # 9 --> (9) 111111111

        # 1
        # 11 * 1 = 11
        # 111 =
