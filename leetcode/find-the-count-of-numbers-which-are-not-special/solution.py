class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        """
        def isSpecial(number):
            total = 0
            for i in range(1, number):
                if number % i == 0:
                    total += 1
                if total == 3:
                    return False
            return total == 2
        """
        """
        res = r - l + 1
        for i in range(l, r + 1):
            if (i ** 0.5) % 1 == 0:
                res -= 1
        return res
        """
        lim = int(math.sqrt(r))
        
        is_prime = [True] * (lim + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, lim):
            if is_prime[i]:
                for j in range(i + i, lim + 1, i):
                    is_prime[j] = False

        special_count = 0
        for i in range(2, lim + 1):
            if is_prime[i]:
                square = i * i
                if l <= square <= r:
                    special_count += 1

        total_count = r - l + 1

        return total_count - special_count
