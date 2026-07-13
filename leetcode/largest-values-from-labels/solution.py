class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:

        values_labels = [[v, l] for v, l in zip(values, labels)]
        values_labels.sort(reverse=True)
        used_amt = defaultdict(int)
        total = 0
        res = 0
        for i in range(len(values_labels)):
            v, l = values_labels[i]
            if used_amt[l] != useLimit and total != numWanted:
                res += v
                used_amt[l] += 1
                total += 1
        return res
