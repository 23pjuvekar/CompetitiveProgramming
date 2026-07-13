class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerful_integers = set()

        if bound <= 0:
            return []

        x_limit = bound if x <= 1 else int(log(bound, x))
        y_limit = bound if y <= 1 else int(log(bound, y))

        for i in range(x_limit + 1):
            for j in range(y_limit + 1):
                value = x**i + y**j
                if value <= bound:
                    powerful_integers.add(value)
                if y == 1:
                    break
                if y == 0:
                    break
            if x == 1:
                break
            if x == 0:
                break
        return list(powerful_integers)
