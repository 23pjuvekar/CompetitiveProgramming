class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        front_score = 0
        rear_score = 0
        n = len(cardPoints)

        for i in range(k):
            front_score += cardPoints[i]

        max_score = front_score

        for i in range(k - 1, -1, -1):
            rear_score += cardPoints[n - (k - i)]
            front_score -= cardPoints[i]
            current_score = rear_score + front_score
            max_score = max(max_score, current_score)

        return max_score
