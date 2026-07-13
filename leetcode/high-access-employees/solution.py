class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:

        def getTime(time):
            return (int(time[:2]) * 60) + (int(time[2:]))

        mp = defaultdict(list)
        for person, time in access_times:
            mp[person].append(time)

        res = []
        for person, times in mp.items():
            times.sort()
            for i in range(len(times) - 2):
                if getTime(times[i + 2]) - getTime(times[i]) < 60:
                    res.append(person)
                    break
        return res
