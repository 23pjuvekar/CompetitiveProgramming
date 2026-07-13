class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        dp = defaultdict(int)
        for cp in cpdomains:
            a = cp.split(" ")
            c = a[1]
            t = int(a[0])
            curr = ""
            arr = c.split(".")
            while arr:
                if curr != "":
                    curr = "." + curr
                curr = arr.pop() + curr
                dp[curr] += t
        
        res = []
        for key, value in dp.items():
            res.append(str(value) + " " + key)
        return res
