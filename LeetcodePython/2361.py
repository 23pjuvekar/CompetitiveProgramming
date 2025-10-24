class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:

        N = len(regular)
        regular_dp = [0] * (N + 1)
        express_dp = [0] * (N + 1)
        total_best_scores = [0] * N

        express_dp[0] = expressCost
        for i in range(1, N + 1):
            regular_dp[i] = min(
                regular_dp[i - 1] + regular[i - 1],
                express_dp[i - 1] + regular[i - 1]
            )

            express_dp[i] = min(
                express_dp[i - 1] + express[i - 1],
                regular_dp[i - 1] + expressCost + express[i - 1]
            )
            
            total_best_scores[i - 1] = min(regular_dp[i], express_dp[i])
        
        return total_best_scores