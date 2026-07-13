class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:

        res = skills.index(max(skills))
        curr = 0
        count = 0
        for i in range(1, len(skills)):
            if skills[curr] < skills[i]:
                curr = i
                count = 1
            else:
                count += 1
            if count == k:
                return curr
        return res
