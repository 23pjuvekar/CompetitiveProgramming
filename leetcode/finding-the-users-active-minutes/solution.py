class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        UAM = defaultdict(set)
        for log in logs:
            UAM[log[0]].add(log[1])
        res = [0] * k
        for user, amt in UAM.items():
            res[len(amt) - 1] += 1
        return res
