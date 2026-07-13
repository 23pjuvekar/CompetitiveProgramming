class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

        total = defaultdict(int)
        most_viewed = {} # creator -> [id, views]
        
        for c, i, v in zip(creators, ids, views):
            total[c] += v
            if c not in most_viewed:
                most_viewed[c] = [i, v]
            else:
                if v > most_viewed[c][1] or (v == most_viewed[c][1] and i < most_viewed[c][0]):
                    most_viewed[c] = [i, v]
        
        max_pop = max(total.values())
        
        ans = []
        for creator, popularity in total.items():
            if popularity == max_pop:
                ans.append([creator, most_viewed[creator][0]])
                
        return ans
