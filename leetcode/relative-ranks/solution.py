class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        score_index = [[score[i], i] for i in range(len(score))]
        score_index.sort(reverse=True)
        res = [""] * len(score)
        for i in range(len(score_index)):
            if i == 0:
                res[score_index[i][1]] = "Gold Medal"
            elif i == 1:
                res[score_index[i][1]] = "Silver Medal"
            elif i == 2:
                res[score_index[i][1]] = "Bronze Medal"
            else:
                res[score_index[i][1]] = str(i+1)
        return res
