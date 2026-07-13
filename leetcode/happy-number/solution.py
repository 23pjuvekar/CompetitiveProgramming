class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()

        while n != 1:
            print(n)
            if n in visited:
                return False
            visited.add(n)
            new_num = 0
            for c in str(n):
                new_num += int(c) * int(c)
            n = new_num
        
        return True
