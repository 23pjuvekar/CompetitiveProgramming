class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        prev = [0, 0]
        res = ""
        for a in target:
            new = [(ord(a) - ord("a")) // 5, (ord(a) - ord("a")) % 5]
            print(new)
            if a == "z":
                while prev[1] < new[1]:
                    prev[1] += 1
                    res += 'R'
                while prev[1] > new[1]:
                    prev[1] -= 1
                    res += 'L'
                while prev[0] > new[0]:
                    prev[0] -= 1
                    res += 'U'
                while prev[0] < new[0]:
                    prev[0] += 1
                    res += 'D'
            else:
                while prev[0] > new[0]:
                    prev[0] -= 1
                    res += 'U'
                while prev[0] < new[0]:
                    prev[0] += 1
                    res += 'D'
                while prev[1] < new[1]:
                    prev[1] += 1
                    res += 'R'
                while prev[1] > new[1]:
                    prev[1] -= 1
                    res += 'L'
            res += '!'
            prev = new
        return res
