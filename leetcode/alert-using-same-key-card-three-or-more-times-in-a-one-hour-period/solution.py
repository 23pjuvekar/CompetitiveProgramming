class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def sub(time1, time2):
            hours = int(time2[:2]) - int(time1[:2])
            minutes = int(time2[3:]) - int(time1[3:])
            return (hours * 60) + minutes

        map_people = defaultdict(deque)
        res = set()

        for person, time in sorted(zip(keyName, keyTime), key=lambda x: x[1]):
            map_people[person].append(time)
            while sub(map_people[person][0], map_people[person][-1]) > 60:
                map_people[person].popleft()
            if len(map_people[person]) > 2:
                res.add(person)
        
        return sorted(res)
