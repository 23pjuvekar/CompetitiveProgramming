class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        res = []
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        def dfs(adj, src):
            if src in adj:
                destinations = list(adj[src])
                while destinations:
                    dest = destinations[0]
                    adj[src].pop(0)
                    dfs(adj, dest)
                    destinations = list(adj[src]) # Backtracking
            res.append(src) # Add node when it is the end

        dfs(adj, "JFK")
        res.reverse()

        if len(res) != len(tickets) + 1:
            return []

        return res
