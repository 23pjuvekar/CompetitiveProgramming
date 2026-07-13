class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:


        res = []
        d = defaultdict(int, {"electronics": 1, "grocery":2, "pharmacy":3, "restaurant":4})

        data = list(zip(code, businessLine, isActive))
        data.sort(key = lambda x:(d[x[1]], x[0]))

        for coupId, busCat, curAct in data:
            if not coupId.replace('_', 'a').isalnum(): continue
            if d[busCat] == 0: continue                         
            if not curAct: continue                             

            res.append(coupId)

        return res
