class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        res = []
        depth = int(math.log2(label))
        
        while label >= 1:
            res.append(label)
            depth -= 1
            min_val = 2 ** depth
            max_val = (2 ** (depth + 1)) - 1

            standard_parent = label // 2
            label = min_val + max_val - standard_parent
            
        return res[::-1]
